import discord
import asyncio
client = discord.Client()
token = 'NzEyOTA3NzAxODgwODgxMjI2.XsYZIg.rni635XiC1VTO894TWnygnrNg4A'
@client.event
async def on_ready():
             print("Logged in as ")
             print(client.user.name)
             print(client.user.id)
             game = discord.Game("상태메세지 내용")
             await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
               if message.content.startswith("큐베야"):
                              await message.channel.send("ㅎㅇ")





client.run(token)