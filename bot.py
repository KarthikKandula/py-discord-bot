# Import required modules
import os
import random
import discord
from dotenv import load_dotenv
import requests
import json

print("Hello World!")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
my_guild = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

client = discord.Client()

def get_quote():
    response = requests.get("https://type.fit/api/quotes")
    json_data = json.loads(response.text)
    quote = json_data[random.randint(0,len(json_data))]['text'] + " - " + json_data[random.randint(0,1642)]['author']
    return(quote)

@client.event
async def on_ready():
    # for guild in client.guilds:
    #     if guild.name == my_guild:
    #         break

    print(f"{client.user} is connected to the following guild:\n ")# f"{guild.name}(id: {guild.id})")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_content = message.content.lower()
    if "flip a coin" in message_content:
        print(f"Flipping a coin for {message.author} ")
        rand_int = random.randint(0, 1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"
        await message.channel.send(results)

    if "hello" in message_content:
        print(f"Hello from {message.author} ")
        await message.channel.send(f"Hello {message.author}")

    if "inspire" in message_content:
        quote = get_quote()
        print(f"Inspired {message.author} ")
        await message.channel.send(quote)

    if "ping" in message_content:
        print(f"Ping detected from {message.author}")
        await ping("Ping back!")

    if "noderun" in message_content:
        print(f"noderun command from {message.author}")
        #cmdresult = os.system("curl localhost:5000/discordcall")

        # Trying to read server call output
        stream = os.popen("curl localhost:5000/discordcall")
        output = stream.read()
        await ping(f"noderun executed successfully with exit code {output} ")

async def ping(pingmsg):
    channel = client.get_channel(827770086948339732)
    await channel.send(pingmsg)

client.run(TOKEN)
