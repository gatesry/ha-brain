#!/usr/bin/env python3
import os
import datetime
from scripts.common import get
from pathlib import Path
import json

def main():
    export_dir = Path("exports")
    export_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_path = export_dir / f"ha_session_context_{timestamp}.txt"

    sections = []
    def add_section(title, data):
        sections.append((title, data))

    # Core sections
    entities = get("states")
    services = get("services")
    add_section("Entities", entities)
    add_section("Services", services)

    # These may require admin token; ignore failures gracefully
    def try_get(name, endpoint):
        try:
            return get(endpoint)
        except Exception as e:
            return {"error": f"Failed to fetch {name}: {e}"}

    areas = try_get("areas", "config/area_registry/list")
    devices = try_get("devices", "config/device_registry/list")
    automations = try_get("automations", "config/automation/config")

    add_section("Areas", areas)
    add_section("Devices", devices)
    add_section("Automations", automations)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Home Assistant Context Export\n")
        f.write(f"# Generated: {timestamp}\n\n")
        for title, data in sections:
            f.write(f"## {title}\n")
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n\n")

    print(f"✅ Export complete: {out_path}")

if __name__ == "__main__":
    main()
