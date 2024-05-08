import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("The bot is ready to use!")
    print("------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello I am The Auto Bot")




@client.event
async def on_member_join(member):
    channel = client.get_channel(1215953106718818326)
    await channel.send("Helloouu")


# To add a random joke when a member joins we can use the RapidAPI and the code for that is given below:


# NOTE : The code commented out below is a demonstration of showing a random joke when the member joins the server , but i wont be using it and also you can use any other type of API on this certain event or any other events.
    # import json
    # import requests
    # jokeurl = "https://joke3.p.rapidapi.com/v1/joke"

    # headers = {
	# "content-type": "application/json",
	# "X-RapidAPI-Key": "e1f3fd936bmsh8300f3bda264e44p1dc04bjsn8e840b92a1d9",
	# "X-RapidAPI-Host": "joke3.p.rapidapi.com"
    # }
    # response = requests.request("GET", jokeurl, headers=headers)

    # print(response.json())

    # await channel.send(response.text)


@client.event 
async def on_member_leave(member):
    channel = client.get_channel(1215953106718818326)
    await channel.send("Goodbye")

# To make this project work you will have to enter your discord token in the brackets below and you can find that discord token at your "discord developer portal"

client.run('Enter Your Token Here')