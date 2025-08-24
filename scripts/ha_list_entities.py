#!/usr/bin/env python3
from scripts.common import get

def main():
    states = get("states")
    print(f"Found {len(states)} entities")
    for s in states:
        print(f"{s.get('entity_id','?')}: {s.get('state','?')}")

if __name__ == "__main__":
    main()
