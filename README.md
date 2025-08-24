# Home Assistant Brain 🧠

**Export your entire Home Assistant setup to enhance AI-powered automation creation**

A powerful context export tool that captures your complete Home Assistant configuration - entities, services, areas, devices, and automations - into a structured format perfect for pasting into AI chat sessions (ChatGPT, Claude, etc.) to get better, more accurate automation suggestions tailored to your specific setup.

## 🎯 Purpose

This tool solves a common problem: **AI assistants don't know your specific Home Assistant setup**. By exporting your complete HA context and providing it to an AI, you can:

- **Generate automations** that use your actual entity names and capabilities
- **Get device-specific suggestions** based on what you actually have installed
- **Create complex scenes and scripts** with proper service calls for your devices
- **Debug existing automations** with full context of your system
- **Plan home automation improvements** based on your current setup

**Credits:**  
Inspired by [Patient_Decision_164 on Reddit](https://www.reddit.com/user/Patient_Decision_164/)

## 🚀 Quick Start

### Prerequisites
- Home Assistant instance (local or remote)
- Python 3.7+ installed
- VS Code (recommended) or any terminal

### Setup (5 minutes)

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/ha-brain.git
cd ha-brain
```

2. **Create a Home Assistant Long-Lived Access Token**
   - Open Home Assistant → Click your profile → **Long-Lived Access Tokens**
   - Click **Create Token** → Name it "HA Brain Export" → Copy the token

3. **Configure your connection**
```bash
cp .env.example .env
# Edit .env with your HA URL and token
```

4. **Install dependencies**
```bash
# Option 1: Using Make
make setup

# Option 2: Manual setup
python -m venv .venv
. .venv/bin/activate  # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
```

5. **Test your connection**
```bash
python scripts/ha_test.py
# Should display your HA version and basic info
```

6. **Export your Home Assistant context**
```bash
python scripts/ha_context_export.py
# Creates timestamped export in exports/ directory
```

The export file can now be copied and pasted into any AI chat session!

## 📋 Typical Workflow

1. **Export your HA context** using this tool
2. **Start a new AI chat session** (ChatGPT, Claude, etc.)
3. **Paste your context** with a message like:
   > "Here's my Home Assistant setup: [paste export]. Please help me create an automation that..."
4. **Get tailored suggestions** using your actual entity names and device capabilities
5. **Copy the generated YAML** directly into Home Assistant

## 💡 Example Use Cases

### Creating Automations
```
"Using my Home Assistant setup above, create an automation that:
- Turns on living room lights at sunset
- Only if someone is home
- Dims them to 40% after 10pm"
```

### Debugging Issues
```
"My motion sensor automation isn't working. Here's my HA context 
and the current automation YAML. What's wrong?"
```

### Optimizing Existing Setup
```
"Based on my devices and current automations, suggest improvements 
for my home security setup"
```

### Complex Scenes
```
"Create a 'Movie Night' scene that:
- Dims specific lights
- Turns off unnecessary devices
- Sets the TV to the right input
Use my actual device names from the context"
```

---

## 🛠️ Additional Tools

### VS Code Integration
If using VS Code, predefined tasks are available via **Command Palette** → **"Run Task"**:
- Setup: Create venv & install
- HA: Test connection
- HA: Create notification (safe)
- HA: Export context

### Testing & Development Scripts

**Safe Connection Test:**
```bash
# Creates a harmless notification in HA
python scripts/ha_create_notification.py --title "Test" --message "Connected!"
```

**List All Entities:**
```bash
# Shows all entity IDs and their current states
python scripts/ha_list_entities.py
```

**Call Any Service (Advanced):**
```bash
# Generic service caller for any HA service
python scripts/ha_call_service.py <domain> <service> [--entity-id ENTITY] [--data '{}']

# Example: Safe test with notification
python scripts/ha_call_service.py persistent_notification create \
  --data '{"title":"Test","message":"Hello from CLI!"}'
```

## 📁 Repository Structure

```
ha-brain/
├── scripts/                      # Core functionality
│   ├── common.py                 # Shared HA API client
│   ├── ha_context_export.py      # Main export tool
│   ├── ha_test.py                # Connection tester
│   ├── ha_list_entities.py       # Entity lister
│   ├── ha_create_notification.py # Safe test action
│   └── ha_call_service.py        # Generic service caller
├── exports/                      # Your exports go here (gitignored)
├── .env.example                  # Template for configuration
├── requirements.txt              # Python dependencies
├── Makefile                      # Convenience commands
└── CLAUDE.md                     # AI assistant instructions
```

## 🔒 Security Notes

- **Never commit your `.env` file** - it contains your access token
- The `.gitignore` file excludes sensitive files automatically
- Exports may contain sensitive information - review before sharing
- Use admin tokens only if you need full access to all HA features

## 🤝 Contributing

Feel free to submit issues and enhancement requests! This tool is designed to be simple and focused on its core purpose: exporting Home Assistant context for AI-assisted automation development.

## 📝 What Gets Exported?

The export includes:
- **All entities** with their current states and attributes
- **Available services** with their parameters
- **Areas** defined in your HA instance
- **Devices** and their capabilities
- **Existing automations** (if accessible with your token)

The export format is optimized for AI consumption while remaining human-readable.

## ⚠️ Troubleshooting

**Connection refused:**
- Check your HA URL includes the port (usually `:8123`)
- Ensure HA is accessible from your machine
- Verify HTTP/HTTPS protocol matches your setup

**401/403 Errors:**
- Regenerate your Long-Lived Access Token
- Ensure token has necessary permissions
- Some endpoints require admin access

**Export is incomplete:**
- Admin tokens provide fullest access
- Non-admin tokens may limit device/area access
- Check script output for any error messages

## 📜 License

MIT License - See LICENSE file for details

---

*Built with ❤️ for the Home Assistant community*
