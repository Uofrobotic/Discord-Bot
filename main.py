# imports
import json
import asyncio
import time
from discord.ext import commands, tasks
import discord as dis

# Turn bot online
class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

# Load initial door status
def load_door_status():
    with open('door-state.json', 'r') as file:
        data = json.load(file)
    return data['door_status']

intents = dis.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", help_command=None, intents=intents)
GUILD_ID = dis.Object(id=server_id)#DISCORD SERVER ID

# Task to update channel name based on door status
@tasks.loop(minutes=1)
async def update_channel_name():
    channel = client.get_channel(CHANNEL_id))#Replace with your channel ID
    time.sleep(15)
    inp = load_door_status()
    #rename channel
    if inp == 1:
        await channel.edit(name="Door Open 🟢")
    elif inp == 0:
        await channel.edit(name="Door Closed 🔴")

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')
    update_channel_name.start()  # Start the loop

#read token
f = open(TOKEN_FILE_NAME, "r")
token = f.read()
f.read()
client.run(token)

