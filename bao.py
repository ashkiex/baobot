import discord
import random
from datetime import datetime
from discord.utils import get

client = discord.Client()

# when someone pings another person, bao will ping again
# "brb" "be right back" "see you guys later" "see u guys" "hungry"
# ratings and emoji reaction to any image sent
# clean up/fine tune code
# time based responses
# create a persistent log
# come here | gif of hamster in hand
# heres/here's | hamster in cup

@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    today = "logs/" + datetime.today().strftime(('%d-%m-%Y')) + ".txt"
    f = open(today, 'w')
    f.write("Successfully initialised at " + datetime.today().strftime('%H:%M:%S'))
    f.write("\n")
    f.close()


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel == member.guild.system_channel:
            await channel.send(f"\*squeak* welcome to SADCATZ, {member.mention}! give me mealworms and/or sunflower seeds and i will love you forever :heart: \n\n*call my name and i'll probably squeak at you*")


@client.event
async def on_message(message):
    f = open("logs/log.txt", 'a')
    if message.author == client.user: # does not reply to bots, including itself
        return

    if "food" in message.content.lower() or "fud" in message.content.lower():
        await message.channel.send("*nyoom*", file=discord.File('media/baorunning.gif'))

    if "bao" in message.content.lower():
        num = random.randint(1, 10)
        if num == 1:
            await message.channel.send('*squeak*')
            f.write("Case 1 at " + datetime.today().strftime('%H:%M:%S') + " on " + datetime.today().strftime('%d-%m-%Y'))
        elif num == 2:
            await message.channel.send('give me treats')
            f.write("Case 1 at " + datetime.today().strftime('%H:%M:%S') + " on " + datetime.today().strftime('%d-%m-%Y'))
        elif num == 3:
            await message.channel.send('*squeak squeak*')
        elif num == 4:
            await message.channel.send('zzZZz')
        elif num == 5:
            await message.channel.send('*SQUEAKKKKKKKKKKKKK*')
        elif num == 6:
            await message.channel.send('*squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak*')
        elif num == 7:
            await message.channel.send('i heard lee jiah is gay')
        elif num == 8:
            await message.channel.send('my owners are the best <3')
        elif num == 9:
            await message.channel.send('I REQUIRE ATTENTION')
        elif num == 10:
            await message.channel.send('rawrX3')
        else:
            await message.channel.send('wtf this message isnt supposed to be sent')

    if "gay" in message.content.lower():
        print(message.author.mention)
        await message.channel.send(f'{message.author.mention} no u gay')

    if "369" in message.content:
        await message.channel.send('singapore bo peh zao')
    elif "69" in message.content:
        await message.channel.send('nice.')

    if "brb" in message.content.lower() or "be right back" in message.content.lower() or "afk" in message.content.lower() or "see ya" in message.content.lower() or "see ya later" in message.content.lower() or "see ya ltr" in message.content.lower() or "see you" in message.content.lower() or "see you later" in message.content.lower() or "see you ltr" in message.content.lower() or "see u" in message.content.lower() or "see u later" in message.content.lower() or "see u ltr" in message.content.lower():
        await message.channel.send("bring back some food *squeak*")

    if "nomnom" in message.content.lower() or "hungry" in message.content.lower() or "nom" in message.content.lower():
        await message.channel.send(file=discord.File("media/nomnom.gif"))

    if len(message.attachments) > 0:
        # emoji reaction
        emotes = []
        server = message.guild
        for emoji in server.emojis:
            emotes.append(emoji)

        await message.add_reaction(random.choice(emotes))

        # rating and comment
        rating = random.randint(0, 10)
        if rating <= 3:
            comments = ["bao not approve.", "*squeaks in hamster*"]
            comment = random.choice(comments)
        elif rating >= 8:
            comments = ["bao approve.", "*squeaks happily*"]
            comment = random.choice(comments)
        else:
            comments = ["could be better", "if it had a sunflower seed or a mealworm *squeak* it probably would have received a better rating."]
            comment = random.choice(comments)

        await message.channel.send(str(rating) + "/10 - " + comment)


client.run('NzAyODAxODMyNDE3ODIwNzc0.XqFcNQ.86FloEyaOdkF9qUlMtV9_83jjLY')
