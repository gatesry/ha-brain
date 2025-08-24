#!/usr/bin/env python3
import argparse
from scripts.common import post

def main():
    parser = argparse.ArgumentParser(description="Create a persistent_notification in Home Assistant (safe demo).")
    parser.add_argument("--title", default="Hello from CLI")
    parser.add_argument("--message", default="This is a test notification from your repo.")
    args = parser.parse_args()

    payload = {"title": args.title, "message": args.message}
    resp = post("services/persistent_notification/create", payload)
    print("✅ Notification created:", resp)

if __name__ == "__main__":
    main()
