# 0rkx Discord Bot

0rkx Bot is a multi-purpose Discord automation bot built with Python and `discord.py`. The current implementation provides a variety of features including a local JSON-backed virtual economy, real-time image manipulation using PIL, server moderation tools, and external API integrations for fetching Reddit memes and COVID-19 statistics.

The project demonstrates how to structure a command-based bot, handle async operations, and manage simple state on the filesystem without requiring a complex backend infrastructure initially.

## Table of Contents

- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Folder Structure](#folder-structure)
- [Architectural Decisions](#architectural-decisions)
- [Data Model](#data-model)
- [Setup Instructions](#setup-instructions)
- [Future Improvements](#future-improvements)
- [Learning Outcomes](#learning-outcomes)
- [License](#license)

## About the Project

This project addresses the need for a versatile Discord bot that can handle typical community engagement tasks—such as economy games, meme generation, and channel moderation. The bot focuses heavily on user interaction, allowing server members to buy/sell virtual items, rob other users, and generate custom meme images using other users' profile pictures.

Currently, the project functions as an early-stage prototype. State is managed locally in `yes.json` rather than a dedicated database, and the architecture prioritizes rapid feature development over high scalability.

## Key Features

### Virtual Economy System
A complete local economy system that allows users to earn, trade, and spend virtual currency.
- **Transactions:** `!deposit`, `!withdraw`, `!send`, and `!rob` for moving money between wallet, bank, and other users.
- **Earning:** `!beg` (with cooldown) and a mini-game `!slots` for gambling.
- **Shop & Inventory:** Users can buy items (`!shop`, `!buy`) and view them (`!bag`). Items can also be sold back (`!sell`).
- **Leaderboard:** `!leaderboard` sorts users based on combined wallet and bank wealth.

### Dynamic Image Manipulation
Uses the `Pillow` library to dynamically generate images by overlaying Discord avatars onto predefined templates.
- **Commands:** `!wanted`, `!spank`, and `!beat`.
- **Implementation:** Fetches avatars as `BytesIO` streams, resizes them, pastes them onto base images (`wanted.png`, `spank.jpg`, etc.), and saves them locally before sending them to the channel.

### External API Integrations
- **Reddit Memes:** `!meme` uses `asyncpraw` to fetch hot posts from `r/memes`.
- **COVID-19 Stats:** `!covid [country]` uses the `requests` module to fetch and display statistics from an external Heroku API.
- **Random Cats:** `!cat` uses `aiohttp` to fetch random cat images.

### Moderation & Utility
- **Channel Controls:** `!lock`, `!unlock`, and `!setslowmode` to manage channel states.
- **User Verification:** `!fraudcheck` compares the user's account creation date to the current date to detect potentially suspicious accounts.
- **Server Info:** `!whois`, `!serverinfo`, and `!channelstats` for detailed Discord entity metrics.

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Core | Python | Main programming language |
| Discord API | `discord.py` | Command handling, events, and gateway communication |
| State | JSON (`yes.json`) | Local file-based storage for user economy data |
| Image Processing | `Pillow` (PIL) | Manipulating and generating dynamic user-based images |
| External APIs | `asyncpraw`, `aiohttp`, `requests` | Fetching Reddit data, cat images, and JSON payloads |

## System Architecture

The bot uses an event-driven architecture based on `discord.ext.commands`.

```txt
Discord User
  ↓
Discord API / Gateway
  ↓
discord.py Command Framework (secretsystems.py)
  ├── Image Processing (Pillow) ← Template Images (spank.jpg, etc.)
  ├── API Integrations (asyncpraw, requests, aiohttp)
  └── Economy Module
        ↓
    Local Filesystem (yes.json)
```

## Folder Structure

Based on the core files:
```txt
/
  secretsystems.py     # Main application entry point and command logic
  yes.json             # Local JSON database for the economy system
  beat.png             # Image template
  beaten.png           # Generated output image
  profile.png          # Generated output image
  spank.jpg            # Image template
  spanked.jpg          # Generated output image
  wanted.png           # Image template
```

## Architectural Decisions

### Local JSON State for Prototyping
The economy system persists data locally in `yes.json`. Every time a transaction occurs, the app reads the JSON file, updates the dictionary, and writes it back synchronously. While this approach creates an IO bottleneck and limits scalability for multiple concurrent users, it is highly practical for early-stage prototyping. It allowed the core logic of transactions, shops, and bags to be built and tested without standing up a Postgres or Redis instance.

### Sync File IO inside Async Functions
The current codebase mixes synchronous file operations (`with open("yes.json")`) and synchronous requests (`requests.get()`) inside an asynchronous `discord.py` event loop. This tradeoff means the bot could block the event loop under heavy load, but it significantly sped up initial development for straightforward API calls and data persistence.

### File-based Image Buffering
Instead of sending image bytes directly back to Discord from memory, the bot saves generated PIL images to disk (e.g., `spanked.jpg`) and then uploads the file. This creates a simple mental model for debugging the generated images.

## Data Model

### Economy User Profile (`yes.json`)
The application stores user state keyed by their Discord ID as a string.

- **`wallet`**: (Float/Int) Money currently on hand. Vulnerable to `!rob`.
- **`bank`**: (Float/Int) Money safely stored in the bank.
- **`bag`**: (Array of Objects) Items purchased from the shop. Each object contains:
  - `item`: Name of the item (e.g., "watch").
  - `amount`: Quantity owned.

## Setup Instructions

### Prerequisites
- Python 3.8+
- A registered Discord Bot Application with an active token.
- Reddit Developer API credentials (for `praw`/`asyncpraw`).

### Installation
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install discord.py praw asyncpraw Pillow requests aiohttp wikipedia
   ```
3. Create `yes.json` if it doesn't exist:
   ```json
   {}
   ```

### Configuration Notes
Currently, API credentials (Discord token, Reddit client ID/secret) are hardcoded directly in `secretsystems.py`. **Do not push active tokens to public repositories.** Before running locally, ensure you replace the existing strings with your actual developer keys or migrate them to environment variables.

### Running Locally
To start the bot, run:
```bash
python secretsystems.py
```

## Future Improvements

- **Environment Variables:** Extract all hardcoded credentials (Discord token, Reddit secret) into a `.env` file using `python-dotenv` for security.
- **Database Integration:** Migrate the `yes.json` economy system to an asynchronous database driver like `aiosqlite` or `asyncpg` to prevent IO blocking and data corruption under high concurrency.
- **Async I/O Compliance:** Replace `requests.get` with `aiohttp` across the codebase to fully utilize the async event loop. Send PIL images via `discord.File` using `BytesIO` directly instead of writing to intermediate disk files.
- **Command Cogs:** Refactor `secretsystems.py` into multiple smaller files using `discord.ext.commands.Cog` to separate the Economy, Image Manipulation, and Moderation domains.

## Learning Outcomes

This project demonstrates strong practical software engineering skills in building event-driven applications. It shows how to integrate multiple third-party services, manage file-based state, compose dynamic media using Pillow, and map complex user interactions (like a virtual economy) into actionable commands. It effectively balances rapid prototyping with feature delivery.

## License
License information has not been specified yet.