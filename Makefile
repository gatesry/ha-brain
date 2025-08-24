SHELL := /bin/bash

.PHONY: setup test notif export

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

test:
	. .venv/bin/activate && python scripts/ha_test.py

notif:
	. .venv/bin/activate && python scripts/ha_create_notification.py --title "VS Code ✅" --message "Hello from Makefile"

export:
	. .venv/bin/activate && python scripts/ha_context_export.py
