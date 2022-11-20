import random

import os
import discord
from discord import app_commands
import datetime

token = os.environ.get('DISCORD_BOT_SECRET')
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="dadjoke", description="Get a dadjoke")
async def dadjoke_dadjoke(interaction):
  embed = discord.Embed(title=random.choice(dj), color=0xFF5733)
  embed.set_footer(text='Type: DadJoke')
  embed.set_author(name="Requested By " + str(interaction.user))
  await interaction.response.send_message(embed=embed)





@client.event
async def on_ready():
  await tree.sync()
  print('We have logged in as {0.user}'.format(client))


client.run(token)
