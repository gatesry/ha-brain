#!/usr/bin/env python3
"""
Updates the Home Assistant export and optionally combines all context files.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Import existing functionality
from scripts.ha_context_export import main as export_ha
from scripts.combine_context import combine_context_files

def update_context(combine=False):
    """Update HA export and optionally combine all files."""
    print("=" * 60)
    print("🔄 Updating Home Assistant Context")
    print("=" * 60)
    
    # Run HA export
    print("\n📥 Exporting latest Home Assistant data...")
    try:
        export_ha()
    except Exception as e:
        print(f"❌ Error exporting HA data: {e}")
        return False
    
    # Copy to context folder
    context_dir = Path("context")
    context_dir.mkdir(exist_ok=True)
    
    # Find latest export
    exports_dir = Path("exports")
    export_files = sorted(exports_dir.glob("ha_session_context_*.txt"))
    
    if export_files:
        latest_export = export_files[-1]
        context_export = context_dir / "3_ha_export.md"
        
        # Copy with header
        with open(latest_export, 'r', encoding='utf-8') as f:
            content = f.read()
        
        with open(context_export, 'w', encoding='utf-8') as f:
            f.write(f"# Home Assistant Export\n")
            f.write(f"*Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            f.write(content)
        
        print(f"✅ HA export copied to context folder")
    
    # Optionally combine all files
    if combine:
        print("\n📦 Combining all context files...")
        output_path = combine_context_files()
        print(f"✅ Combined context saved to: {output_path}")
        return output_path
    
    return True

def main():
    """Main update process."""
    parser = argparse.ArgumentParser(description="Update HA context and optionally combine files")
    parser.add_argument(
        "--combine", "-c",
        action="store_true",
        help="Combine all context files after updating"
    )
    
    args = parser.parse_args()
    
    result = update_context(combine=args.combine)
    
    if result:
        print("\n" + "=" * 60)
        print("✅ Context update complete!")
        if args.combine and isinstance(result, Path):
            print(f"\n📋 Ready to copy: {result}")
        print("=" * 60)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()