import discord
import random
from datetime import datetime

client = discord.Client()

today = "logs/" + datetime.today().strftime(('%d-%m-%Y')) + ".txt"

def logtime():
    time = datetime.today().strftime('%H:%M:%S | ')
    return time


@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    f = open(today, 'a')
    f.write("Successfully initialised at " + datetime.today().strftime('%H:%M:%S'))
    f.write("\n")
    f.close()


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if channel == member.guild.system_channel:
            await channel.send("*squeaks sadly*  someone left the server :'( i hope they come back and bring me sunflower seeds")
    print(logtime() + str(member) + " left " + str(member.guild))
    f = open(today, 'a')
    f.write(logtime() + str(member) + " left " + str(member.guild))
    f.write('\n')
    f.close()


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel == member.guild.system_channel:
            await channel.send(f"*squeak*  welcome to SADCATZ, {member.mention}! give me mealworms and/or sunflower seeds and i will love you forever :heart: \n\n*call my name and i'll probably squeak at you*")
    print(logtime() + str(member) + " joined " + str(member.guild))
    f = open(today, 'a')
    f.write(logtime() + str(member) + " joined " + str(member.guild))
    f.write('\n')
    f.close()


@client.event
async def on_message(message):
    # f.open(today, 'a')
    if message.author == client.user: # does not reply to bots, including itself
        return

    if "food" in message.content.lower() or "fud" in message.content.lower() or "sunflower seed" in message.content.lower() or "mealworm" in message.content.lower():
        await message.channel.send("*nyoom*", file=discord.File('media/baorunning.gif'))
        print("fooooood??????")
        f = open(today, 'a')
        f.write(logtime() + "someone said food")
        f.write('\n')
        f.close()

    if "baohelp" in message.content.lower() or "bao help" in message.content.lower():
        await message.channel.send("""*squeak squeak*  here's a little self-introduction! my name is bao, and i was born roughly mid October 2019. i was adopted when i was about 3 weeks old and have been living the best life since.
        
here are somethings i like:
- food (especially sunflower seeds, and mealworms :heart:)
- *nice* numbers
- running into people's hands
- eating
- rating pictures
- some memes (WIP)
- called out to

and some things i don't like (WIP lengmao):
- being called fat (i just have big bones !!)

and that's about it! i don't bite (usually) so play with me!

*please let my owner know if u have any suggestions on improvements or similar.*""")

        print("intro")
        f = open(today, 'a')
        f.write(logtime() + "someone needed a self-introduction")
        f.write('\n')
        f.close()

    elif "bao" in message.content.lower():
        num = random.randint(1, 10)
        if num == 1:
            await message.channel.send('*squeak*')
        elif num == 2:
            await message.channel.send('give me treats')
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
        print("yes?")
        f = open(today, 'a')
        f.write(logtime() + "someone said called my name")
        f.write('\n')
        f.close()

    if "fatfuck" in message.content.lower() or "fat fuck" in message.content.lower() or "fatass" in message.content.lower() or "fat ass" in message.content.lower():
        await message.channel.send("*squeak*  thats rude! im not fat, im just round. *squeak squeak*  you may refer to me as a chonky boi, though.")
        print(":'(")
        f = open(today, 'a')
        f.write(logtime() + "someone said called me fat :(")
        f.write('\n')
        f.close()

    if "heres" in message.content.lower() or "here's" in message.content.lower():
        await message.channel.send("*squeak* the motherfking tea?", file=discord.File("media/teacup.jpg"))
        print("TEA")
        f = open(today, 'a')
        f.write(logtime() + "someone said a meme")
        f.write('\n')
        f.close()

    if "come" in message.content.lower() or "here" in message.content.lower():
        num = random.randint(1, 3)
        if num == 1:
            await message.channel.send(file=discord.File("media/hand2.jpg"))
        elif num == 2:
            await message.channel.send(file=discord.File("media/hand3.jpg"))
        elif num == 3:
            await message.channel.send(file=discord.File("media/hand3.png"))
        print("")
        f = open(today, 'a')
        f.write(logtime() + "i went into someones hand")
        f.write('\n')
        f.close()

    if "gay" in message.content.lower():
        await message.channel.send(f'{message.author.mention} no u gay')
        print("haha GAYYYYY")
        f = open(today, 'a')
        f.write(logtime() + "someone said the g-word")
        f.write('\n')
        f.close()

    if "369" in message.content:
        await message.channel.send('singapore bo peh zao')
        print("369")
        f = open(today, 'a')
        f.write(logtime() + "kapohkapoh popo kiao")
        f.write('\n')
        f.close()
    elif "69" in message.content:
        await message.channel.send('nice.')
        print("nice.")
        f = open(today, 'a')
        f.write(logtime() + "someone said 69")
        f.write('\n')
        f.close()

    if "brb" in message.content.lower() or "be right back" in message.content.lower() or "afk" in message.content.lower() or "see ya" in message.content.lower() or "see ya later" in message.content.lower() or "see ya ltr" in message.content.lower() or "see you" in message.content.lower() or "see you later" in message.content.lower() or "see you ltr" in message.content.lower() or "see u" in message.content.lower() or "see u later" in message.content.lower() or "see u ltr" in message.content.lower():
        await message.channel.send("bring back some food *squeak*")
        print("somebody went away :(")
        f = open(today, 'a')
        f.write(logtime() + "someone went away")
        f.write('\n')
        f.close()

    if "nomnom" in message.content.lower() or "hungry" in message.content.lower() or "nom" in message.content.lower():
        await message.channel.send(file=discord.File("media/nomnom.gif"))
        print("omnomnom")
        f = open(today, 'a')
        f.write(logtime() + "omnomnom")
        f.write('\n')
        f.close()

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

        print("i rated a pic")
        f = open(today, 'a')
        f.write(logtime() + "i rated a pic")
        f.write('\n')
        f.close()

    for i in message.guild.members:
        if i.mentioned_in(message):
            await message.channel.send(i.mention)

f = open("token.txt", "r")
token = f.read()
client.run(token)
