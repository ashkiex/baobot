import discord
import random


class Hamster:
    def __init__(self, hunger, energy, mood):
        self.__hunger = hunger
        self.__energy = energy
        self.__mood = mood

    def set_hunger(self, hunger):
        self.__hunger = hunger

    def set_energy(self, energy):
        self.__energy = energy

    def set_mood(self, mood):
        self.__mood = mood

    def get_hunger(self):
        return self.__hunger

    def get_energy(self):
        return self.__energy

    def get_mood(self):
        return self.__mood

    async def msgResponse(self, message):
        if "food" in message.content.lower() or "fud" in message.content.lower() or "sunflower seed" in message.content.lower() or "mealworm" in message.content.lower():
            await message.channel.send("*nyoom*", file=discord.File('media/baorunning.gif'))
            print("fooooood??????")
            # line = "someone said food @" + str(message.guild)
            # Logger.set_line(line)
            # Logger.log()

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
            # line = "someone needed a self-introduction @" + str(message.guild)
            # log(line)

        elif "bao" in message.content.lower() or "chonk" in message.content.lower() or "chonky" in message.content.lower() or "chonkyboi" in message.content.lower() or "chonky boi" in message.content.lower():
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
            # line = "someone said called my name @" + str(message.guild)
            # log(line)

        if "fatfuck" in message.content.lower() or "fat fuck" in message.content.lower() or "fatass" in message.content.lower() or "fat ass" in message.content.lower() or "fat" in message.content.lower() or "phat" in message.content.lower() or "fatty" in message.content.lower():
            await message.channel.send("*squeak*  thats rude! im not fat, im just round. *squeak squeak*  you may refer to me as a chonky boi, though.")
            print(":'(")
            # line = "someone said called me fat :( @" + str(message.guild)
            # log(line)

        if "heres" in message.content.lower() or "here's" in message.content.lower():
            await message.channel.send("*squeak* the motherfking tea?", file=discord.File("media/teacup.jpg"))
            print("TEA")
            # line = "someone said a meme @" + str(message.guild)
            # log(line)
        elif "come" in message.content.lower() or "here" in message.content.lower():
            num = random.randint(1, 3)
            if num == 1:
                await message.channel.send(file=discord.File("media/hand2.jpg"))
            elif num == 2:
                await message.channel.send(file=discord.File("media/hand3.jpg"))
            elif num == 3:
                await message.channel.send(file=discord.File("media/hand.png"))
            print("hand")
            # line = "i went into someones hand @" + str(message.guild)
            # log(line)

        if "gay" in message.content.lower():
            await message.channel.send(f'{message.author.mention} no u gay')
            print("haha GAYYYYY")
            # line = "someone said the g-word @" + str(message.guild)
            # log(line)

        if "369" in message.content:
            await message.channel.send('singapore bo peh zao')
            print("369")
            # line = "kapohkapoh popo kiao @" + str(message.guild)
            # log(line)
        elif "69" in message.content:
            await message.channel.send('nice.')
            print("nice.")
            # line = "someone said 69 @" + str(message.guild)
            # log(line)

        if "brb" in message.content.lower() or "be right back" in message.content.lower() or "afk" in message.content.lower() or "see ya" in message.content.lower() or "see ya later" in message.content.lower() or "see ya ltr" in message.content.lower() or "see you" in message.content.lower() or "see you later" in message.content.lower() or "see you ltr" in message.content.lower() or "see u" in message.content.lower() or "see u later" in message.content.lower() or "see u ltr" in message.content.lower():
            await message.channel.send("bring back some food *squeak*")
            print("somebody went away :(")
            # line = "someone went away @" + str(message.guild)
            # log(line)

        if "nomnom" in message.content.lower() or "hungry" in message.content.lower() or "nom" in message.content.lower():
            await message.channel.send(file=discord.File("media/nomnom.gif"))
            print("omnomnom")
            # line = "omnomnom @" + str(message.guild)
            # log(line)

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
            # line = "i rated a pic @" + str(message.guild)
            # log(line)

        for i in message.guild.members:
            if i.mentioned_in(message) and not message.mention_everyone:
                await message.channel.send(f"{i.mention} *squeak*  please bring me some food")
