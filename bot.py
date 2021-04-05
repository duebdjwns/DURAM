import discord

client = discord.Client()
token = "ODI3MTE0OTQ2ODYwOTQxMzEz.YGWU0g.C4rMNOGPy_A51dP0tM-2ZuJ0yOQ"

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.content.startswith("나는 살아있다."):
        await message.channel.send("pong!")

client.run(token)