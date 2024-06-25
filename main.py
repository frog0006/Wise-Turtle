#used replit

import os
import discord
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_quote():
    response = requests.get ("https://zenquotes.io/api/random")
    json_data = json.loads (response.text)
    quote = json_data[0]['q'] + "   -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!quote'):
        quote = get_quote()
        await message.channel.send(quote)


try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
