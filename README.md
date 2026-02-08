# Python Discord Bot

Minimal Discord bot built with `discord.py` and `python-dotenv`.

## Setup

Create a virtual environment in `.venv`:

```bash
python3 -m venv .venv
```

Add your bot token in `.env`:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

## Run

```bash
source .venv/bin/activate
pip install -r requirements.txt
python src/bot.py
```

The bot responds to:
- `!ping`
- `!hello`
