import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
import requests
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

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
    source = FFmpegPCMAudio('Discord Bot\Fantasize.mp3')
    player = voice.play(source)

# This shows a random quote from the list , You could use an API too. 
@client.command(pass_context=True)
async def quote(ctx):
    quoteList = ["The most disastrous thing that you can ever learn is your first programming language. - Alan Kay",
                 "Talk is cheap. Show me the code. - Linus Torvalds",
                 "Perl – The only language that looks the same before and after RSA encryption. - Keith Bostic",
                 "If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger Dijkstra",
                 "Programming is like sex. One mistake and you have to support it for the rest of your life. - Michael Sinz",
                 "The trouble with programmers is that you can never tell what a programmer is doing until it’s too late. - Seymour Cray",
                 "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. - John Woods",
                 "Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the universe trying to produce bigger and better idiots. So far, the universe is winning. - Rick Cook",
                 "You can't have great software without a great team, and most software teams behave like dysfunctional families. - Jim McCarthy",
                 "Programming isn't about what you know; it's about what you can figure out. - Chris Pine"
                 ]  # Put your quotes here!

    await ctx.send(str(random.choice(quoteList)))

# This shows how many members are online and how many are offline on discord server.

# Note that "idle" and "dnd" are also considered as online
@client.command()
async def stats(ctx):
    online_members = []
    offline_members = []
    for member in ctx.guild.members:
        if member.status is not discord.Status.offline:
            online_members.append(member.name)
        else:
            offline_members.append(member.name)

    embed = discord.Embed(title=f'"{ctx.guild.name}" Stats', color=0x000)
    embed.add_field(name="Member Count", value=ctx.guild.member_count)
    embed.add_field(name="Online", value=f'{len(online_members)} :green_circle:', inline=True)
    embed.add_field(name="Offline", value =f'{len(offline_members)} :red_circle:', inline = True)
    await ctx.send(embed=embed)


# Making it so that the bot detects specific words.


# @client.event
# async def on_message(message):
#     if message.content == "hi":
#         await message.delete()
#         await message.channel.send("Prevent from using that word")


# This is the code to detect certain words and make the bot auto delete it with a warning, "Will Add and API or .txt file later"
# @client.listen('on_message')
# async def on_message(message):
#     if message.content == "Hate":
#         await message.delete()
#         await message.channel.send("Prevent from using that word")



@client.listen('on_message')
    # This makes the bot roll a dice whenever you write '?roll' in the chat.
async def on_message(message):
    if message.content.startswith('?roll'):
        sides = 6
        try:
            sides = int(message.content.split()[1])
        except IndexError:
            pass
        except ValueError:
            await message.channel.send("Please provide a valid number of sides for the dice")
            return

        result = random.randint(1, sides)
        await message.channel.send(f'You rolled a {result} on a {sides}-sided dice!')


    # Gives a random xkcd comic image
    if message.content.startswith('?xkcd'):
        r = requests.get(
            "https://xkcd.com/info.0.json",
            proxies={'http': '222.255.169.74:8080'},
            timeout=5
        )

        data = r.json()
        comic_num = data['num']
        comic_img = data['img']
        comic_alt = data['alt']

        # Construct the comic message
        comic_message = f"**XKCD Comic #{comic_num}**\n{comic_alt}\n{comic_img}"

        # Send the comic message to the Discord channel
        await message.channel.send(comic_message)



# This is for kick or ban command.
@client.command()
@has_permissions(kick_members = True)
async def kick(ctx, member:discord.Member,*,reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'User {member} has been kicked.')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have permission to kick people")


@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member,*,reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been Banned.')

@kick.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have permission to ban people")



# To make this project work you will have to enter your discord token in the brackets below and you can find that discord token at your "discord developer portal"
client.run('Enter Your Token Here')