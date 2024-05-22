import discord
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
import random
import requests
from discord import Member
from datetime import datetime, timedelta
from discord.ext.commands import has_permissions, MissingPermissions
import os
import asyncio

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())


client = commands.Bot(command_prefix='?', intents=discord.Intents.all())
NASA_API_KEY = os.getenv(
    'NASA_API_KEY', 'Enter Your Nasa Api Key Here')
# You can get your api key from : https://api.nasa.gov/

@client.event
async def on_ready():
    print("The bot is ready to use!")
    print("------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello I am The Cheese Bot")




@client.event
async def on_member_join(member):
    channel = client.get_channel(1242832943257358356)
    if channel:
        # Create the welcome message
        welcome_message = (
            f"Welcome to the server, {member.mention}! 🧀\n\n"
            "We're thrilled to have you here! 🎉\n\n"
            "Make sure to check out the Cheesy Bot and introduce yourself. Have a great time! \n\n"
            "If you have any other ideas for the Cheese Bot , feel free to share it in the ideas channel."
        )

        # Send the welcome message to the welcome channel
        await channel.send(welcome_message)


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

jokes = [
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why did the cheese cross the road? To get to the other slice!",
    "What type of cheese is made backward? Edam!",
    "How do you handle dangerous cheese? Caerphilly.",
    "What’s a cheese’s favorite music? R’n’Brie.",
    "What did the cheese say when it looked in the mirror? Halloumi!",
    "What cheese surrounds a medieval castle? Moat-zarella.",
    "Why doesn’t cheddar like to party with crackers? Because it always gets grilled!"
]

facts = [
    "Cheese is the most stolen food in the world!",
    "There are over 2,000 varieties of cheese.",
    "The world's most expensive cheese is made from donkey milk.",
    "Cheese can be made from the milk of cows, goats, sheep, and even buffalo.",
    "The largest cheese ever made weighed over 57,000 pounds.",
    "Ancient Egyptians included cheese in their tomb offerings.",
    "The holes in Swiss cheese are called 'eyes'.",
    "Cheese was first made over 4,000 years ago by accident."
]

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
        await message.channel.send(f'You rolled a cheesy {result} on a {sides}-sided cheese dice!')


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

    
    # Embed for socials
    if message.content.startswith('?socials'):
            # Create an embed with social media links
            embed = discord.Embed(
                title="Follow Me on Social Media!", color=0x1DA1F2)
            embed.add_field(
                name="Twitter", value="[Click here](https://twitter.com/soninesh2006)", inline=False)
            embed.add_field(
                name="Instagram", value="[Click here](https://instagram.com/soninesh2006)", inline=False)
            embed.add_field(
                name="YouTube", value="[Click here](https://www.youtube.com/c/www.youtube.com/@neshsoni7844)", inline=False)
            embed.add_field(
                name="Github", value="[Click here](https://www.github.com/EpicNesh26)", inline=False)

            embed.set_footer(text="Thank you for following!")

        # Send the embed to the Discord channel
            await message.channel.send(embed=embed)

    # Intro
    if message.content.startswith('?cheese'):
        # Create the funny introduction text for Cheese Bot
        intro_text = (
            "**Hello! I'm Cheese Bot!**\n\n"
            "🧀 I'm your friendly neighborhood bot made entirely of cheese! 🧀\n\n"
            "**What I Can Do:**\n"
            "- Crack cheesy jokes\n"
            "- Serve up cheesy facts\n"
            "- Roll cheesy dice\n\n"
            "**Fun Fact:**\n"
            "Did you know that cheese is the most stolen food in the world? Now that's a big cheese heist!\n\n"
            "Stay cheesy, my friends! 🧀"
        )

        # Send the introduction text to the Discord channel
        await message.channel.send(intro_text)

    # Cheesy Joke
    if message.content.startswith('?joke'):
        # Select a random joke from the list
        joke = random.choice(jokes)
        
        # Send the joke to the Discord channel
        await message.channel.send(joke)


    # Cheesy fact
    elif message.content.startswith('?fact'):
        # Select a random fact from the list
        fact = random.choice(facts)
        
        # Send the fact to the Discord channel
        await message.channel.send(fact)


    # Rock Paper Scissor game
    if message.content.startswith('?rps'):
        user_choice = message.content.split()[1].lower()
        possible_choices = ['rock', 'paper', 'scissors']

        if user_choice not in possible_choices:
            await message.channel.send("Please choose either rock, paper, or scissors.")
            return

        bot_choice = random.choice(possible_choices)
        result = determine_winner(user_choice, bot_choice)

        await message.channel.send(f'You chose: {user_choice}\nCheese Bot chose: {bot_choice}\nResult: {result}')

    if message.content.startswith('?role'):
        # Send a message with a cheese emoji reaction
        role_message = await message.channel.send("React with 🧀 to get the Cheese Lover role!")

        # Add the cheese emoji reaction to the message
        await role_message.add_reaction('🧀')


def determine_winner(user, bot):
    if user == bot:
        return "It's a tie!"
    elif (user == 'rock' and bot == 'scissors') or (user == 'paper' and bot == 'rock') or (user == 'scissors' and bot == 'paper'):
        return "You win!"
    else:
        return "You lose!"

# Reacting add function to add the cheese role
@client.event
async def on_reaction_add(reaction, user):
    # Check if the reaction is to the role assignment message and from a non-bot user
    if reaction.message.content == "React with 🧀 to get the Cheese Lover role!" and not user.bot:
        # Check if the reacted emoji is the cheese emoji
        if str(reaction.emoji) == '🧀':
            # Get the server the user reacted in
            guild = reaction.message.guild

            # Get or create the Cheese Lover role
            cheese_role = discord.utils.get(guild.roles, name="Cheese Lover")
            if not cheese_role:
                cheese_role = await guild.create_role(name="Cheese Lover", color=discord.Color.gold())

            # Assign the Cheese Lover role to the user
            await user.add_roles(cheese_role)
            await user.send("You've been granted the Cheese Lover role!")

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


@client.command()
async def apod(ctx):
    apod_data = get_apod()
    if apod_data:
        embed = discord.Embed(
            title=apod_data['title'], description=apod_data['explanation'], color=discord.Color.blue())
        embed.set_image(url=apod_data['url'])
        embed.set_footer(text=f"Date: {apod_data['date']}")
        await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry, I couldn't fetch the Astronomy Picture of the Day.")


def get_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

    r = requests.get(
            url,
            proxies={'http': '222.255.169.74:8080'},
            timeout=5
        )

    if r.status_code == 200:
        data = r.json()
        return {
            'title': data['title'],
            'explanation': data['explanation'],
            'url': data['url'],
            'date': data['date']
        }
    else:
        return None

# A BIG DISCORD BOT INTRO 

@client.command()
async def cheesebot(ctx):
    emb = discord.Embed(title="🧀 Cheese Bot Profile 🧀", color=discord.Color.gold())
    emb.set_thumbnail(url=client.user.avatar.url)
    
    emb.add_field(name="Name", value="Cheese Bot", inline=False)
    emb.add_field(name="Purpose", value="To spread cheesy goodness and fun throughout the server!", inline=False)
    emb.add_field(name="Features", value=(
        "🧀 Introduction: `?intro`\n"
        "🧀 My Socials: `?socials`\n"
        "🧀 Say Hello: `?hello`\n"
        "🧀 Stats: `?stats`\n"
        "🧀 Assign Cheese Role: `?role`\n"
        "🧀 Cheesy Dice Roll: `?roll`\n"
        "🧀 Cheese Jokes: `?joke`\n"
        "🧀 Cheese Facts: `?fact`\n"
        "🧀 Random Normal Quote: `?quote`\n"
        "🧀 Xkcd Comic Image: `?xkcd`\n"
        "🧀 Play Rock Paper Scissors: `?rps`\n"
        "🧀 Astronomy Picture of the Day: `?apod`\n"
        "🧀 Join Voice Channel: `?join`\n"
        "🧀 Leave Voice Channel: `?leave`\n"
        "🧀 Play a song: `?play`\n"
        "🧀 Pause a song: `?pause`\n"
        "🧀 Resume a song: `?resume`\n"
        "🧀 Stop a song: `?stop`\n"
        "🧀 Daily Challenge: `?dailychallenge`\n"
        "🧀 Set Reminder: `?remindme <time> <msg>`\n"


    ), inline=False)
    emb.add_field(name="Fun Fact", value="Did you know? There are over 1,800 different types of cheese in the world!", inline=False)
    emb.add_field(name="Developer", value="Nesh", inline=False)
    emb.set_footer(text=f"Bot Name: {client.user.name}")
    
    await ctx.send(embed=emb)


challenges = [
    "Share a photo of something that makes you happy.",
    "Write a short story or a poem.",
    "Do 10 push-ups and share your experience.",
    "Learn a new fact and share it with the server.",
    "Draw a picture and share it with the community.",
    "Listen to a new song and share your thoughts.",
    "Cook a new recipe and share a photo.",
    "Take a walk and describe what you see.",
    "Compliment someone in the server.",
    "Share a motivational quote."
]

last_challenge_date = None
# Task to send a daily challenge


@tasks.loop(hours=24)
async def send_daily_challenge():
    global last_challenge_date
    current_date = datetime.utcnow().date()

    # Check if a challenge has already been sent today
    if last_challenge_date == current_date:
        return

    # Select a random challenge
    challenge = random.choice(challenges)

    # Specify the channel ID where the challenge should be posted
    channel_id = 1215953106718818326  # Replace with your channel ID
    channel = client.get_channel(channel_id)

    if channel:
        embed = discord.Embed(title="🧀 Daily Challenge 🧀",
                              description=challenge, color=discord.Color.dark_gold())
        embed.set_footer(text=f"Date: {current_date}")
        await channel.send(embed=embed)

    # Update the last challenge date
    last_challenge_date = current_date

# Command to manually trigger the daily challenge (useful for testing)


@client.command()
async def dailychallenge(ctx):
    global last_challenge_date
    current_date = datetime.utcnow().date()

    # Select a random challenge
    challenge = random.choice(challenges)

    embed = discord.Embed(title="🧀 Daily Challenge 🧀",
                          description=challenge, color=discord.Color.gold())
    embed.set_footer(text=f"Date: {current_date}")
    await ctx.send(embed=embed)

    # Update the last challenge date
    last_challenge_date = current_date



# To set reminders
reminders = {}
@client.command()
async def remindme(ctx, time: int, *, message: str):
    reminder_time = datetime.utcnow() + timedelta(minutes=time)
    reminders[ctx.author.id] = (reminder_time, message)

    embed = discord.Embed(
        title="Reminder Set",
        description=f"I will remind you in {time} minutes.",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

    await asyncio.sleep(time * 60)  # Convert minutes to seconds

    if ctx.author.id in reminders and reminders[ctx.author.id][0] == reminder_time:
        embed = discord.Embed(
            title="Reminder",
            description=message,
            color=discord.Color.blue()
        )
        await ctx.send(f"{ctx.author.mention}", embed=embed)
        del reminders[ctx.author.id]

# Task to check reminders periodically
@tasks.loop(seconds=30)
async def check_reminders():
    current_time = datetime.utcnow()
    to_remove = []
    for user_id, (reminder_time, message) in reminders.items():
        if current_time >= reminder_time:
            user = client.get_user(user_id)
            if user:
                embed = discord.Embed(
                    title="Reminder",
                    description=message,
                    color=discord.Color.blue()
                )
                await user.send(embed=embed)
                to_remove.append(user_id)
    for user_id in to_remove:
        del reminders[user_id]


# To make this project work you will have to enter your discord token in the brackets below and you can find that discord token at your "discord developer portal"
client.run('Enter Your Token Here')