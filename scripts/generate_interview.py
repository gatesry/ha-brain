#!/usr/bin/env python3
"""
Interactive interview script to generate personalized household information file.
Creates a structured profile for AI assistants to better understand your context.
"""

import json
import os
from datetime import datetime
from pathlib import Path

def ask_question(prompt, options=None, allow_multiple=False, required=True):
    """Ask user a question and return their response."""
    print(f"\n{prompt}")
    
    if options:
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        print()
        
        if allow_multiple:
            print("  (Enter multiple numbers separated by commas, or press Enter to skip)")
        else:
            print("  (Enter number, or press Enter to skip)")
        
        response = input("> ").strip()
        
        if not response and not required:
            return None
            
        if allow_multiple:
            try:
                indices = [int(x.strip()) - 1 for x in response.split(",")]
                return [options[i] for i in indices if 0 <= i < len(options)]
            except (ValueError, IndexError):
                return ask_question(prompt, options, allow_multiple, required)
        else:
            try:
                index = int(response) - 1
                if 0 <= index < len(options):
                    return options[index]
            except (ValueError, IndexError):
                pass
            return ask_question(prompt, options, allow_multiple, required)
    else:
        response = input("> ").strip()
        if not response and required:
            print("This field is required. Please provide an answer.")
            return ask_question(prompt, options, allow_multiple, required)
        return response if response else None

def generate_household_profile():
    """Interactive interview to build household profile."""
    print("=" * 60)
    print("🏠 Home Assistant Household Profile Generator")
    print("=" * 60)
    print("\nI'll ask you some questions to build a profile that helps AI")
    print("assistants provide better, more personalized automation suggestions.")
    print("\nYour answers will be saved locally and never shared.")
    print("=" * 60)
    
    profile = {}
    
    # Dwelling Details
    print("\n📍 DWELLING INFORMATION")
    profile['dwelling_type'] = ask_question(
        "What type of dwelling do you have?",
        ["Single-family house", "Apartment", "Townhouse", "Condo", "Other"]
    )
    
    profile['dwelling_size'] = ask_question(
        "Approximate size? (e.g., '1500 sq ft, 3 bedrooms')"
    )
    
    profile['floors'] = ask_question(
        "How many floors?",
        ["Single story", "Two story", "Three+ story", "Split level"]
    )
    
    profile['layout'] = ask_question(
        "Briefly describe your layout (e.g., 'Open concept, master bedroom upstairs')",
        required=False
    )
    
    # Household Members
    print("\n👨‍👩‍👧‍👦 HOUSEHOLD MEMBERS")
    profile['adults'] = ask_question("How many adults live here?")
    profile['children'] = ask_question("How many children? (enter 0 if none)")
    
    if int(profile['children']) > 0:
        profile['children_ages'] = ask_question("Children's age ranges? (e.g., '5-10 years')")
    
    profile['pets'] = ask_question(
        "Do you have pets?",
        ["No pets", "Dog(s)", "Cat(s)", "Both dogs and cats", "Other pets"],
        allow_multiple=True
    )
    
    # Schedule
    print("\n⏰ DAILY SCHEDULE")
    profile['work_schedule'] = ask_question(
        "What's your primary work situation?",
        ["Work from home", "Office/on-site", "Hybrid", "Shift work", "Retired", "Other"]
    )
    
    profile['wake_time'] = ask_question("Typical wake time on weekdays? (e.g., '6:30 AM')")
    profile['bed_time'] = ask_question("Typical bedtime on weekdays? (e.g., '10:30 PM')")
    
    profile['weekend_different'] = ask_question(
        "Is your weekend schedule significantly different?",
        ["Yes", "No"]
    )
    
    # Home Assistant Goals
    print("\n🎯 HOME ASSISTANT GOALS")
    profile['primary_goals'] = ask_question(
        "What are your main goals with Home Assistant? (select multiple)",
        [
            "Energy savings",
            "Security",
            "Convenience",
            "Accessibility",
            "Entertainment",
            "Climate comfort",
            "Pet care",
            "Plant care"
        ],
        allow_multiple=True
    )
    
    profile['automation_philosophy'] = ask_question(
        "What's your automation philosophy?",
        [
            "Fully automated - minimal interaction",
            "Mostly automated with manual overrides",
            "Balanced automation and control",
            "Minimal automation - prefer manual control"
        ]
    )
    
    profile['tech_level'] = ask_question(
        "How would you rate your technical comfort level?",
        ["Beginner", "Intermediate", "Advanced", "Expert"]
    )
    
    # Environmental Preferences
    print("\n🌡️ ENVIRONMENTAL PREFERENCES")
    profile['temp_day'] = ask_question("Preferred daytime temperature? (e.g., '72F' or '22C')")
    profile['temp_night'] = ask_question("Preferred nighttime temperature?")
    profile['lighting_pref'] = ask_question(
        "Lighting preference?",
        ["Bright", "Dim", "Varies by room", "Natural light when possible"]
    )
    
    # Pain Points and Successes
    print("\n💭 CURRENT EXPERIENCE")
    profile['pain_points'] = ask_question(
        "What frustrates you about your current setup? (optional)",
        required=False
    )
    
    profile['success_stories'] = ask_question(
        "What automations work well for you? (optional)",
        required=False
    )
    
    profile['additional_context'] = ask_question(
        "Any other context that would help AI assistants? (optional)",
        required=False
    )
    
    return profile

def format_profile_markdown(profile):
    """Convert profile dictionary to formatted markdown."""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    md = f"""# Personal Household Information
*Generated: {timestamp}*

## 🏠 Dwelling Details
**Type**: {profile.get('dwelling_type', 'Not specified')}
**Size**: {profile.get('dwelling_size', 'Not specified')}
**Floors**: {profile.get('floors', 'Not specified')}
**Layout**: {profile.get('layout', 'Not specified')}

## 👨‍👩‍👧‍👦 Household Members
**Adults**: {profile.get('adults', '0')}
**Children**: {profile.get('children', '0')}"""
    
    if int(profile.get('children', 0)) > 0:
        md += f"\n**Children Ages**: {profile.get('children_ages', 'Not specified')}"
    
    if profile.get('pets'):
        md += f"\n**Pets**: {', '.join(profile['pets'])}"
    
    md += f"""

## ⏰ Daily Schedule
**Work Situation**: {profile.get('work_schedule', 'Not specified')}
**Weekday Wake Time**: {profile.get('wake_time', 'Not specified')}
**Weekday Bedtime**: {profile.get('bed_time', 'Not specified')}
**Weekend Different**: {profile.get('weekend_different', 'No')}

## 🎯 Home Assistant Goals
**Primary Goals**: {', '.join(profile.get('primary_goals', ['Not specified']))}
**Automation Philosophy**: {profile.get('automation_philosophy', 'Not specified')}
**Technical Level**: {profile.get('tech_level', 'Not specified')}

## 🌡️ Environmental Preferences
**Daytime Temperature**: {profile.get('temp_day', 'Not specified')}
**Nighttime Temperature**: {profile.get('temp_night', 'Not specified')}
**Lighting Preference**: {profile.get('lighting_pref', 'Not specified')}"""
    
    if profile.get('pain_points'):
        md += f"""

## 😤 Current Pain Points
{profile['pain_points']}"""
    
    if profile.get('success_stories'):
        md += f"""

## ✅ Success Stories
{profile['success_stories']}"""
    
    if profile.get('additional_context'):
        md += f"""

## 📝 Additional Context
{profile['additional_context']}"""
    
    return md

def main():
    """Main interview process."""
    profile = generate_household_profile()
    
    # Create context directory if it doesn't exist
    context_dir = Path("context")
    context_dir.mkdir(exist_ok=True)
    
    # Generate markdown
    markdown_content = format_profile_markdown(profile)
    
    # Save to file
    output_path = context_dir / "4_personal_info.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("\n" + "=" * 60)
    print("✅ Profile generated successfully!")
    print(f"📁 Saved to: {output_path}")
    print("\nYou can edit this file manually to add or modify information.")
    print("=" * 60)
    
    # Also save as JSON for potential future use
    json_path = context_dir / "personal_info.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)

if __name__ == "__main__":
    main()