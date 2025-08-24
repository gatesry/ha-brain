# 🔧 Troubleshooting Guide

Common issues and solutions for Home Assistant Brain export tool.

## Connection Issues

### ❌ Error: "Connection refused" or "Failed to connect"

**Possible Causes & Solutions:**

1. **Wrong URL format**
   - ✅ Correct: `http://homeassistant.local:8123`
   - ❌ Wrong: `homeassistant.local` (missing protocol and port)
   - ❌ Wrong: `http://homeassistant.local` (missing port)

2. **Home Assistant not accessible**
   ```bash
   # Test connectivity first
   curl http://homeassistant.local:8123/api/
   # or
   ping homeassistant.local
   ```

3. **Using wrong protocol (HTTP vs HTTPS)**
   - Local usually uses `http://`
   - Remote/DuckDNS usually uses `https://`

4. **Network issues**
   - Try using IP address instead: `http://192.168.1.100:8123`
   - Ensure you're on the same network as HA
   - Check if HA is actually running

### ❌ Error: "401 Unauthorized" or "403 Forbidden"

**Solutions:**

1. **Invalid or expired token**
   - Create a new token in HA
   - Make sure you copy the ENTIRE token (it's very long!)
   - Don't include quotes around the token in .env

2. **Token lacks permissions**
   - Use an admin account to create the token
   - Some exports require elevated permissions

3. **Token format in .env**
   ```bash
   # Correct - no quotes
   HA_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI...
   
   # Wrong - with quotes
   HA_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI..."
   ```

## Export Issues

### ⚠️ Warning: "Failed to fetch areas/devices/automations"

**This is usually OK!** Non-admin tokens may not have access to all endpoints.

**To get full export:**
1. Create token with an admin account
2. Or ignore these warnings - entity and service data is usually sufficient

### ❌ Error: "No module named 'requests'"

**Solution:**
```bash
# Make sure you're in virtual environment
source .venv/bin/activate  # Mac/Linux
# or
.venv\Scripts\activate  # Windows

# Then install dependencies
pip install requests python-dotenv
```

### ❌ Error: "No such file or directory: '.env'"

**Solution:**
```bash
# Copy the example file first
cp .env.example .env

# Then edit .env with your settings
```

## Environment Issues

### ❌ "python: command not found"

**Solutions:**

1. **Install Python 3.7+**
   - Windows: Download from python.org
   - Mac: `brew install python3`
   - Linux: `sudo apt install python3`

2. **Use python3 command instead**
   ```bash
   python3 -m venv .venv
   python3 scripts/ha_context_export.py
   ```

### ❌ "Permission denied" errors

**Mac/Linux Solution:**
```bash
chmod +x scripts/*.py
```

### ❌ Virtual environment not activating

**Windows PowerShell:**
```powershell
# Enable script execution first
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**
```cmd
.venv\Scripts\activate.bat
```

## Configuration Issues

### ❓ How to find my Home Assistant URL?

1. **Local network (most common):**
   - Try: `http://homeassistant.local:8123`
   - Or find IP in router: `http://192.168.X.X:8123`

2. **Docker installation:**
   - Usually: `http://localhost:8123`
   - Or: `http://127.0.0.1:8123`

3. **Remote access:**
   - DuckDNS: `https://your-name.duckdns.org:8123`
   - Nabu Casa: `https://your-id.ui.nabu.casa`

### ❓ Where do I find the Long-Lived Access Token?

1. Open Home Assistant
2. Click your user profile (bottom left)
3. Scroll to bottom
4. Find "Long-Lived Access Tokens"
5. Click "CREATE TOKEN"
6. Name it (e.g., "HA Brain")
7. **COPY IMMEDIATELY** - you can't see it again!

## Export File Issues

### ❓ Export file is empty or very small

**Possible causes:**
1. Connection failed silently - check your URL and token
2. No entities in HA - check HA is configured
3. Token lacks permissions - use admin token

### ❓ Can't find export file

**Default location:** `exports/ha_session_context_[timestamp].txt`

```bash
# List exports
ls exports/  # Mac/Linux
dir exports  # Windows
```

## Using with AI Assistants

### ❓ AI says "I can't see your Home Assistant configuration"

**Solution:** Make sure you:
1. Copy the ENTIRE export file content
2. Paste it in the same message as your request
3. Explicitly mention it's your HA configuration

**Good prompt example:**
> "Here is my Home Assistant configuration export:
> [PASTE ENTIRE EXPORT]
> 
> Using the entities above, please create an automation that..."

### ❓ AI generates automations with wrong entity names

**Solution:** 
- Ensure your export is complete
- Explicitly ask AI to use your actual entity IDs
- Provide specific examples from your export

## Advanced Debugging

### Enable verbose output

Edit `scripts/common.py` and add:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Test individual components

```bash
# Test connection only
python scripts/ha_test.py

# List entities only
python scripts/ha_list_entities.py

# Create safe notification
python scripts/ha_create_notification.py --title "Test" --message "Working!"
```

### Manual API test

```bash
# Replace with your URL and token
curl -X GET \
  "http://homeassistant.local:8123/api/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## Still Need Help?

1. **Check HA logs:** Settings → System → Logs
2. **Verify HA version:** Should be recent (2023.x or newer)
3. **Try the simple test first:** `python scripts/ha_test.py`
4. **Create an issue:** GitHub repository issues page

## Common Success Indicators

✅ **Successful connection test:**
```
Home Assistant Version: 2024.1.0
Installation Type: Home Assistant OS
```

✅ **Successful export:**
```
✅ Export complete: exports/ha_session_context_2024-01-15_10-30-45.txt
```

✅ **File contains:**
- List of all your entities
- Available services
- Areas and devices (if admin token)
- Current automations

---

Remember: Most issues are related to URL format or token problems. Double-check these first!