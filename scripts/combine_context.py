#!/usr/bin/env python3
"""
Combines all 4 context files into a single file for easy copy/paste into AI chats.
"""

import os
from pathlib import Path
from datetime import datetime

def read_file_safely(filepath):
    """Read a file and return its contents, or return a placeholder if not found."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"[File not found: {filepath}]"
    except Exception as e:
        return f"[Error reading {filepath}: {e}]"

def combine_context_files():
    """Combine all 4 context files into a single output."""
    context_dir = Path("context")
    exports_dir = Path("exports")
    exports_dir.mkdir(exist_ok=True)
    
    # Define the 4 files in order
    files = [
        ("1_boot_instructions.md", "🚀 AI BOOT INSTRUCTIONS"),
        ("2_persona.md", "🤖 AI PERSONA CONFIGURATION"),
        ("3_ha_export.md", "🏠 HOME ASSISTANT EXPORT"),
        ("4_personal_info.md", "👤 PERSONAL HOUSEHOLD INFORMATION")
    ]
    
    # Build combined content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    combined = f"""# COMPLETE HOME ASSISTANT AI CONTEXT
Generated: {timestamp}

This document contains all context needed for AI assistants to provide
personalized Home Assistant automation assistance.

{"=" * 60}

"""
    
    # Add each file
    for filename, section_title in files:
        filepath = context_dir / filename
        
        combined += f"\n# {section_title}\n"
        combined += "=" * 60 + "\n\n"
        
        if filename == "3_ha_export.md":
            # For HA export, try to use the latest export
            export_files = sorted(exports_dir.glob("ha_session_context_*.txt"))
            if export_files:
                content = read_file_safely(export_files[-1])
            else:
                content = "[No HA export found. Run: python scripts/ha_context_export.py]"
        else:
            content = read_file_safely(filepath)
        
        combined += content
        combined += "\n\n" + "=" * 60 + "\n"
    
    # Add footer
    combined += """

# END OF CONTEXT

AI Assistant: I have loaded all 4 context files including:
1. Your interaction preferences and boot instructions
2. My persona configuration
3. Your complete Home Assistant setup with all entities and devices
4. Your household information and automation goals

I'm ready to help you create automations using your actual device IDs 
and tailored to your specific needs. What would you like to automate?
"""
    
    # Save combined file
    output_filename = f"complete_context_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    output_path = exports_dir / output_filename
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(combined)
    
    return output_path

def main():
    """Main combination process."""
    print("=" * 60)
    print("📦 Combining all context files...")
    print("=" * 60)
    
    output_path = combine_context_files()
    
    print(f"\n✅ Combined context created successfully!")
    print(f"📁 Saved to: {output_path}")
    print(f"\n📋 File size: {os.path.getsize(output_path):,} bytes")
    print("\n" + "=" * 60)
    print("📋 TO USE:")
    print("1. Open the file above")
    print("2. Select all text (Ctrl+A / Cmd+A)")
    print("3. Copy (Ctrl+C / Cmd+C)")
    print("4. Paste into your AI chat session")
    print("=" * 60)

if __name__ == "__main__":
    main()