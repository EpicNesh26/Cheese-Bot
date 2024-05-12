import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

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
    # jokeurl = "USE YOUR OWN URL FROM RAPIDAPI"

    # headers = {
	# "content-type": "application/json",
	# "X-RapidAPI-Key": "Enter Your API KEY HERE",
	# "X-RapidAPI-Host": "SAME HERE"
    # }
    # response = requests.request("GET", jokeurl, headers=headers)

    # print(response.json())

    # await channel.send(response.text)


@client.event 
async def on_member_leave(member):
    channel = client.get_channel(1215953106718818326)
    await channel.send("Goodbye")



# This is for the Voice Channel join or leave.
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        await ctx.send("I have joined the voice channel")
        
    else: 
        await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command")
        await ctx.send("You are not in vc")


@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I Left the voice channel")
    else:
        await ctx.send("The bot is not connected to a voice channel")



# This is for pause
@client.command(pass_context = True)
async def pause(ctx):
    # What this does is it is calling the discord package and inside is calling the utils of the voice that is playing.
    voice = discord.utils.get(client.voice_client,guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Nothing is playing")

# This is for resume
@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_client,guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("No audio is paused.")


# This is for stop 
@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
    voice.stop()



# This is for play
@client.command(pass_context = True)
async def play(ctx):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio('Discord Bot\Ariana Grande - Fantasize (Audio).mp3')
    player = voice.play(source)

# To make this project work you will have to enter your discord token in the brackets below and you can find that discord token at your "discord developer portal"
client.run('Enter Your Token Here')