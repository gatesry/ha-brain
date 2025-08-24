# Home Assistant Automation Examples

This document provides example prompts and use cases for using your exported Home Assistant context with AI assistants.

## How to Use These Examples

1. First, export your Home Assistant context using: `python scripts/ha_context_export.py`
2. Copy the contents of the export file from the `exports/` directory
3. Start a new chat with your AI assistant (ChatGPT, Claude, etc.)
4. Paste your context followed by one of these example prompts
5. The AI will generate automations using your actual device names and capabilities

## Example Prompts for AI Assistants

### 🏠 Basic Home Automations

**Lighting Automation:**
```
Using my Home Assistant setup above, create an automation that:
- Turns on the porch light 30 minutes before sunset
- Turns it off at sunrise
- Only runs when we're home (use my presence detection entities)
```

**Morning Routine:**
```
Create a morning routine automation that triggers at 7 AM on weekdays:
- Gradually increase bedroom lights over 5 minutes
- Turn on kitchen lights
- Set the thermostat to day mode
- Start the coffee maker if it's a smart plug
Use my actual device names from the context.
```

### 🔒 Security Automations

**Away Mode:**
```
Create a comprehensive "Away Mode" automation package that:
- Arms the alarm when everyone leaves
- Turns off all lights except security lights
- Sets thermostats to away temperature
- Sends a notification when armed
- Randomly turns on/off lights in the evening to simulate presence
```

**Intrusion Alert:**
```
Build an intrusion detection automation that:
- Triggers when any door/window sensor opens while armed
- Turns on all lights
- Sends critical notifications to all phones
- Takes a camera snapshot if available
- Triggers the siren/alarm if present
```

### 🌡️ Climate Control

**Smart Thermostat:**
```
Create a smart climate automation that:
- Adjusts temperature based on room occupancy
- Lowers temperature at night (10 PM)
- Pre-heats/cools before arrival (using location)
- Considers outside temperature if available
Please use my actual climate entities and sensors.
```

### 🎬 Scene-Based Automations

**Movie Night Scene:**
```
Create a "Movie Night" scene and automation:
- Dims living room lights to 20%
- Turns off all other lights
- Closes blinds/curtains if motorized
- Sets TV backlighting if available
- Pauses when motion detected (bathroom break)
- Can be triggered by voice or button
```

**Dinner Time:**
```
Build a dinner scene that:
- Sets dining room lights to warm white at 60%
- Turns on accent lighting
- Plays dinner playlist on speakers if available
- Turns off TV
- Can be scheduled or manually triggered
```

### 💡 Advanced Automations

**Adaptive Lighting:**
```
Create an adaptive lighting system that:
- Adjusts brightness based on time of day
- Changes color temperature (cool during day, warm at night)
- Considers ambient light sensors
- Respects manual overrides for 2 hours
- Only affects lights that support these features
```

**Energy Saving:**
```
Design an energy optimization automation that:
- Turns off devices in empty rooms
- Adjusts AC/heating based on occupancy
- Notifies about devices left on unusually long
- Tracks high-consumption periods
- Suggests optimization based on usage patterns
```

### 🔧 Troubleshooting Requests

**Debug Automation:**
```
Here's my Home Assistant context and a broken automation:
[paste automation YAML]

The automation should turn on lights when motion is detected but it's not working. 
What's wrong and how do I fix it?
```

**Optimization Request:**
```
Review my existing automations in the context above and suggest:
- Which ones could be combined
- Any that might conflict
- Missing automations that would be useful
- Performance improvements
```

### 📱 Notification Automations

**Smart Alerts:**
```
Create a smart notification system that:
- Alerts when doors/windows left open for 10+ minutes
- Notifies about devices left on when leaving home
- Sends daily summary of energy usage
- Alerts for unusual activity patterns
- Uses actionable notifications where possible
```

### 🚗 Arrival/Departure

**Welcome Home:**
```
Create a "Welcome Home" automation that:
- Triggers when I arrive (using device tracker)
- Disarms security
- Turns on pathway lights (sunset to sunrise only)
- Sets comfortable temperature
- Announces arrival on speakers if configured
- Adjusts based on time of day
```

**Leaving Home:**
```
Build a "Leaving Home" routine that:
- Checks all windows/doors are closed
- Turns off all lights and non-essential devices
- Arms the security system after 5 minutes
- Sets climate to away mode
- Sends confirmation notification
- Can be triggered by location or manually
```

## Tips for Better AI Responses

1. **Be Specific**: Instead of "turn on lights", specify "turn on lights when motion detected after sunset"

2. **Include Conditions**: Mention time ranges, presence detection, weather conditions, etc.

3. **Describe Desired Behavior**: Explain what should happen in different scenarios

4. **Ask for Explanations**: Request comments in the YAML to understand the logic

5. **Iterate**: Start simple and ask the AI to add complexity gradually

6. **Provide Context**: Mention your specific needs, like "I work from home" or "I have pets"

## Common Patterns to Request

- **Presence-based**: "Only when someone is home"
- **Time-based**: "Between sunset and 11 PM"
- **Conditional**: "If temperature above 25°C"
- **Sequential**: "Then wait 5 minutes and..."
- **Adaptive**: "Adjust based on outside brightness"
- **Override-aware**: "Unless manually controlled in last hour"
- **Fail-safe**: "With a timeout of 30 minutes"

## Testing Your Automations

After the AI generates an automation:

1. **Review entity names**: Ensure all entities exist in your HA
2. **Check service calls**: Verify services and parameters are valid
3. **Test conditions**: Manually trigger to test logic
4. **Monitor logs**: Check HA logs for any errors
5. **Start simple**: Test basic version before adding complexity

Remember: The AI can only work with the entities and services you've exported. Make sure your export is complete and up-to-date for best results!