# 🚀 Quick Start Guide - 5 Minutes to Export

Get your Home Assistant context exported for AI assistance in under 5 minutes!

## Prerequisites Checklist
- [ ] Home Assistant instance running
- [ ] Python 3.7+ installed (`python --version`)
- [ ] Admin access to your Home Assistant

## Step-by-Step Setup

### 1️⃣ Get Your Access Token (1 minute)
1. Open Home Assistant in your browser
2. Click your profile picture (bottom left)
3. Scroll down to **Long-Lived Access Tokens**
4. Click **CREATE TOKEN**
5. Name it: "HA Brain Export"
6. **COPY THE TOKEN** (you won't see it again!)

### 2️⃣ Download & Configure (2 minutes)

**Option A: Using Git**
```bash
git clone https://github.com/yourusername/ha-brain.git
cd ha-brain
```

**Option B: Download ZIP**
1. Download the repository as ZIP
2. Extract to your desired location
3. Open terminal/command prompt in that folder

### 3️⃣ Configure Connection (1 minute)
```bash
# Copy the example config
cp .env.example .env

# Edit .env file with your text editor
# Set these two lines:
# HA_URL=http://homeassistant.local:8123  (your HA address)
# HA_TOKEN=eyJ0eXAiOi...  (paste your long token here)
```

**Common HA URLs:**
- Local: `http://homeassistant.local:8123`
- Local IP: `http://192.168.1.100:8123` 
- Remote: `https://your-home.duckdns.org:8123`

### 4️⃣ Install & Run (1 minute)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install requests python-dotenv
python scripts/ha_context_export.py
```

**Mac/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install requests python-dotenv
python scripts/ha_context_export.py
```

### 5️⃣ Success! 🎉

Your export is saved in: `exports/ha_session_context_[timestamp].txt`

## Using Your Export with AI

1. Open the export file in `exports/` folder
2. Copy ALL contents (Ctrl+A, Ctrl+C)
3. Start a new ChatGPT or Claude chat
4. Paste with a message like:

> "Here's my Home Assistant setup: [PASTE]
> 
> Please help me create an automation that turns on my living room lights at sunset only when someone is home."

## Troubleshooting

**"Connection refused"**
- Check your HA_URL includes `:8123`
- Try your local IP instead of `homeassistant.local`
- Ensure HA is running

**"401 Unauthorized"**
- Your token may be wrong - create a new one
- Make sure you copied the ENTIRE token

**"File not found"**
- Make sure you're in the `ha-brain` directory
- Run `ls` (Mac/Linux) or `dir` (Windows) to check files

## Need More Help?

- See [README.md](README.md) for detailed documentation
- Check [EXAMPLES.md](EXAMPLES.md) for automation ideas
- Review [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues

---

**Pro Tip:** Save your export before making major HA changes - it's a great backup of your entity list and automation logic!