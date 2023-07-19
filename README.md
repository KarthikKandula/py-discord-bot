# Python Discord Bot - py-discord-bot

Create a Discord Bot using Python

Install all modules in `requirements.txt` using command `pip install -r requirements.txt`

## How to add `DISCORD_TOKEN` & `DISCORD_GUILD` to `.env` file
Its good practice to read secrets such as discord token into the program from an environment variable. Create an `.env` file on all machines that will be running this bot code

### Create a file named `.env` in the same directory as `bot.py`
Sample `.env` file

    # .env
    DISCORD_TOKEN={your-bot-token}
    DISCORD_GUILD={your-guild-name}

Replace placeholders `{your-bot-token}` and `{your-guild-name}` with actual values
> **`{your-bot-token}`** - your bot's token on *Bot* page on the Developer portal and click *Copy* under *TOKEN* section  
> **`{your-guild-name}`** - name of the server that the bot is in
