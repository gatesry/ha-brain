#!/usr/bin/env python3
from scripts.common import get, pretty

def main():
    info = get("")
    version = info.get("version", "unknown")
    user = info.get("user", {}).get("name", "unknown")
    print("✅ Connected to Home Assistant")
    print(f"• Version: {version}")
    print(f"• User: {user}")
    # Fetch a couple safe endpoints
    services = get("services")
    states = get("states")
    print(f"• Services domains: {', '.join(sorted(services.keys())[:10])} ...")
    print(f"• Entity count: {len(states)}")

if __name__ == "__main__":
    main()
