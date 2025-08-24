# Home Assistant Brain

A minimal, ready‑to‑publish repo that lets you connect to **Home Assistant** from your **VS Code terminal** and run safe actions, export context, and explore services/entities.

**Credits:**  
Inspired by [Patient_Decision_164 on Reddit](https://www.reddit.com/user/Patient_Decision_164/)

> Safe default action included: create a `persistent_notification` in Home Assistant so you can verify connectivity without touching lights or critical devices.

---

## Quick Start

1) **Create a Home Assistant Long‑Lived Access Token**
   - Home Assistant UI → **Profile** → **Long‑Lived Access Tokens** → **Create Token** → copy it.

2) **Clone or unzip this repo** and open it in **VS Code**.

3) **Set environment variables** by copying `.env.example` to `.env` and filling in values:

```bash
cp .env.example .env
# Edit .env to set HA_URL and HA_TOKEN
```

4) **Create a Python virtual env and install deps** (or use the VS Code task):
```bash
python -m venv .venv
. .venv/bin/activate  # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
```

5) **Test the connection** (prints basic info and your HA version):
```bash
python scripts/ha_test.py
```

6) **Create a safe notification in HA** (good first live action):
```bash
python scripts/ha_create_notification.py --title "VS Code ✅" --message "Hello from your repo!"
```

7) **Export your Home Assistant context** (entities, services, areas, devices, automations) to `exports/`:
```bash
python scripts/ha_context_export.py
```

---

## VS Code Tasks (no typing required)

Open the **Command Palette** → “**Run Task**” → choose any of:

- **Setup: Create venv & install**
- **HA: Test connection**
- **HA: Create notification (safe)**
- **HA: Export context**

Tasks are defined in `.vscode/tasks.json`.

---

## Call Any Service (advanced)
You can call any HA service using `scripts/ha_call_service.py`:

```bash
# Example: turn on a light (replace with your entity_id)
python scripts/ha_call_service.py light turn_on --entity-id light.living_room --data '{"brightness":200}'
```

**Usage:**
```text
python scripts/ha_call_service.py <domain> <service> [--entity-id ENTITY] [--data '{...json...}']
```

> Tip: start with `persistent_notification.create` to test safely:
```bash
python scripts/ha_call_service.py persistent_notification create --data '{"title":"From CLI","message":"It works!"}'
```

---

## Repo Layout

```
.
├── .env.example              # Copy to .env and fill in values
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
├── exports/                  # Context exports written here
├── scripts/
│   ├── common.py             # Shared HA helpers (auth, GET/POST)
│   ├── ha_call_service.py    # Generic service caller
│   ├── ha_context_export.py  # Dumps entities/services/areas/devices/automations
│   ├── ha_create_notification.py  # Safe demo action
│   ├── ha_list_entities.py   # Lists entity_id + state
│   └── ha_test.py            # Connectivity + basic info
└── .vscode/
    ├── extensions.json
    ├── launch.json
    └── tasks.json
```

---

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: HA Brain repo"
gh repo create --public --source .  # or create manually on GitHub and set remote
git push -u origin main
```

---

## Notes

- Scripts use only the official **Home Assistant REST API**.
- The default export pulls entities, services, areas, devices, and automation configs where permitted by your token.
- If some endpoints return 401/403, ensure your token belongs to an admin account or remove those sections from the exporter.
