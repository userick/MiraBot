import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'helped')
client.run('NDI2ODUxMTMyODIwOTQ2OTQ1.DZb_vw.AbuMg7_NgPrjkQvaAHg5gh7-MNY')
