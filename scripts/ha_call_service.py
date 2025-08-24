#!/usr/bin/env python3
import argparse
import json
from scripts.common import post

def main():
    p = argparse.ArgumentParser(description="Call any Home Assistant service via REST API")
    p.add_argument("domain", help="e.g., light, switch, persistent_notification")
    p.add_argument("service", help="e.g., turn_on, turn_off, create")
    p.add_argument("--entity-id", help="Optional entity_id")
    p.add_argument("--data", help="Optional JSON payload for service")
    args = p.parse_args()

    body = {}
    if args.entity_id:
        body["entity_id"] = args.entity_id
    if args.data:
        try:
            body.update(json.loads(args.data))
        except json.JSONDecodeError as e:
            raise SystemExit(f"Invalid JSON for --data: {e}")

    endpoint = f"services/{args.domain}/{args.service}"
    resp = post(endpoint, body)
    print("✅ Service call OK:", resp)

if __name__ == "__main__":
    main()
