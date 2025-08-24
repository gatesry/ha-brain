# CLAUDE.md - AI Assistant Context

This file provides guidance to AI assistants (Claude, ChatGPT, etc.) when helping users work with Home Assistant exports and automation creation.

## Repository Purpose

This repository is a **Home Assistant context export tool** designed to:
1. Export complete HA configuration (entities, services, areas, devices, automations)
2. Provide this context to AI assistants for better automation suggestions
3. Enable AI to use actual entity names and device capabilities from the user's setup

## When Users Provide Exported Context

When a user pastes their HA export, you should:
- Use their **actual entity IDs** (e.g., `light.living_room_main` not generic names)
- Reference their **specific services and capabilities**
- Consider their **areas and device relationships**
- Build upon their **existing automations** when suggesting improvements
- Provide **copy-paste ready YAML** that will work immediately

## Quick Setup Guide

When helping users set up this tool:

```bash
# 1. Clone repository
git clone https://github.com/[username]/ha-brain.git
cd ha-brain

# 2. Configure environment
cp .env.example .env
# Edit .env with:
# - HA_URL: Full URL with port (e.g., http://homeassistant.local:8123)
# - HA_TOKEN: Long-lived access token from HA profile

# 3. Setup Python environment
python -m venv .venv
. .venv/bin/activate  # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt

# 4. Test connection
python scripts/ha_test.py

# 5. Export context
python scripts/ha_context_export.py
# Output saved to exports/ha_session_context_[timestamp].txt
```

## Common User Requests

### "Help me create an automation"
1. Ask for their exported context if not provided
2. Use their actual entity names from the export
3. Provide complete, working YAML
4. Explain any complex logic or conditions

### "My automation isn't working"
1. Request their export AND the problematic automation YAML
2. Check entity IDs match their actual devices
3. Verify service calls use correct parameters
4. Look for timing/condition issues

### "Optimize my setup"
1. Review their existing automations from the export
2. Identify redundancies or inefficiencies
3. Suggest consolidations using their actual entities
4. Recommend new automations based on unused devices

## Architecture Details

**Core Components:**
- `scripts/common.py`: Shared HA REST API client
- `scripts/ha_context_export.py`: Main export tool
- `scripts/ha_test.py`: Connection tester
- `.env`: Configuration (never commit!)

**Export Contents:**
- **Entities**: All entity IDs with current states and attributes
- **Services**: Available service calls with parameters
- **Areas**: Defined areas/rooms in the HA instance
- **Devices**: Physical devices and their capabilities
- **Automations**: Existing automation configurations

**API Patterns:**
- Uses official Home Assistant REST API
- Bearer token authentication
- JSON responses with full entity details
- Graceful fallback for permission errors

## Automation Best Practices

When creating automations from exported context:

1. **Use Specific Entity IDs**
   ```yaml
   # Good - uses actual entity from export
   entity_id: light.living_room_ceiling
   
   # Bad - generic placeholder
   entity_id: light.example
   ```

2. **Match Service Parameters to Capabilities**
   ```yaml
   # Check if entity supports the feature
   service: light.turn_on
   data:
     brightness_pct: 50  # Only if light is dimmable
     color_name: blue    # Only if light supports color
   ```

3. **Consider Existing Automations**
   - Check for conflicts with current automations
   - Suggest disabling overlapping automations
   - Build complementary logic

4. **Respect Device Types**
   - Don't suggest color for non-RGB lights
   - Check if sensors are binary or numeric
   - Verify device classes (motion, door, temperature)

## Common Issues & Solutions

**Connection Problems:**
- Verify HA_URL includes port (:8123)
- Check HTTP vs HTTPS
- Ensure local network access

**Permission Errors:**
- Admin tokens provide fullest access
- Some endpoints need elevated permissions
- Areas/devices may require admin access

**Export Failures:**
- Token might be expired
- HA instance might be updating
- Network connectivity issues

## Example Automation Templates

When users ask for common automations, adapt these using their actual entities:

**Motion-Activated Lights:**
```yaml
alias: Motion Lights - [Room Name]
trigger:
  - platform: state
    entity_id: [their.motion.sensor]
    to: 'on'
condition:
  - condition: numeric_state
    entity_id: sun.sun
    attribute: elevation
    below: 0
action:
  - service: light.turn_on
    entity_id: [their.light.entity]
```

**Climate Schedule:**
```yaml
alias: Climate Schedule
trigger:
  - platform: time
    at: "07:00:00"
action:
  - service: climate.set_temperature
    entity_id: [their.climate.entity]
    data:
      temperature: 21
```

Always adapt templates to use the user's specific entities and capabilities!