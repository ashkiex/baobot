import discord
import random
import logging


class MessageResponse:

    def __init__(self):
        self.__foodResponse = {"food", "fud", "seed", "mealworm", "nut", "sunflower"}
        self.__baoHelpResponse = {"baohelp", "bao help"}
        self.__baoResponse = {"bao", "chonk"}
        self.__baoFatResponse = {"fat", "phat"}
        self.__baoTeaResponse = {"heres", "here's"}
        self.__baoHandResponse = {"come", "here"}
        self.__baoGayResponse = {"gay", "ghey"}
        self.__bao369Response = {"369"}
        self.__bao69Response = {"69"}
        self.__baoBRBResponse = {"brb", "be right back", "be right bak", "see ya", "see ya later", "see ya ltr", "see you", "see you later", "see you ltr", "afk", "see u", "see u later", "see u ltr"}
        self.__baoNomResponse = {"nom", "hungry", "hungery", "h u n g r y", "h u n g e r y"}

    async def getHamsterResponse(self, message):
        # print(message.content.lower())
        # print(self.__foodResponse)
        await self.baoPhotoResponse(message)
        await self.baoMentionResponse(message)

        for i in self.__foodResponse:
            if i in message.content.lower():
                # print("Test")
                await self.foodResponse(message)
                return  # so it doesnt send more than one of the same response
            # else:
            # print("fail")

        for i in self.__baoHelpResponse:
            if i in message.content.lower():
                # print("Test")
                await self.baoHelpResponse(message)
                return

        for i in self.__baoResponse:
            if i in message.content.lower():
                # print("Test")
                await self.baoResponse(message)
                return

        for i in self.__baoFatResponse:
            if i in message.content.lower():
                # print("Test")
                await self.baoFatResponse(message)
                return

        for i in self.__baoTeaResponse:
            if i in message.content.lower():
                # print("Test")
                await self.baoTeaResponse(message)
                return

        for i in self.__baoHandResponse:
            if i in message.content.lower():
                # print("Test")
                await self.baoHandResponse(message)
                return

        for i in self.__baoGayResponse:
            if i in message.content.lower():
                # print("Test")
                await self.baoGayResponse(message)
                return

        for i in self.__bao369Response:
            if i in message.content.lower():
                # print("Test")
                await self.bao369Response(message)
                return

        for i in self.__bao69Response:
            if i in message.content.lower():
                # print("Test")
                await self.bao69Response(message)
                return

        for i in self.__baoBRBResponse:
            if i in message.content.lower():
                # print("Test")
                await self.baoBRBResponse(message)
                return

        for i in self.__baoNomResponse:
            if i in message.content.lower():
                # print("Test")
                await self.baoNomResponse(message)
                return



    async def foodResponse(self, message):
        # foodResponse = ["food", "fud", "seed", "mealworm", "nut", "sunflower"]
        # if message.content.lower() in foodResponse:
        await message.channel.send("*nyoom*", file=discord.File('media/baorunning.gif'))
        print("fooooood??????")
        # line = "someone said food @" + str(message.guild)
        # Logger.set_line(line)
        # Logger.log()

    async def baoHelpResponse(self, message):
        # baoHelpResponse = ["baohelp", "bao help"]
        # if message.content.lower() in baoHelpResponse:
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

    async def baoResponse(self, message):
        # baoResponse = ["bao", "chonk"]
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
            await message.channel.send(
                '*squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak squeak*')
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

    async def baoFatResponse(self, message):
        # baoFatResponse = ["fat", "phat"]
        await message.channel.send("*squeak*  thats rude! im not fat, im just round. *squeak squeak*  you may refer to me as a chonky boi, though.")
        print(":'(")
        # line = "someone said called me fat :( @" + str(message.guild)
        # log(line)

    async def baoTeaResponse(self, message):
        # baoMTFTeaResponse = ["here's", "heres"]
        await message.channel.send("*squeak* the motherfking tea?", file=discord.File("media/teacup.jpg"))
        print("TEA")
        # line = "someone said a meme @" + str(message.guild)
        # log(line)

    async def baoHandResponse(self, message):
        # elif "come" in message.content.lower() or "here" in message.content.lower():
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

    async def baoGayResponse(self, message):
        # if "gay" in message.content.lower():
            await message.channel.send(f'{message.author.mention} no u gay')
            print("haha GAYYYYY")
            # line = "someone said the g-word @" + str(message.guild)
            # log(line)

    async def bao369Response(self, message):
        # if "369" in message.content:
            await message.channel.send('singapore bo peh zao')
            print("369")
            # line = "kapohkapoh popo kiao @" + str(message.guild)
            # log(line)

    async def bao69Response(self, message):
        # elif "69" in message.content:
            await message.channel.send('nice.')
            print("nice.")
            # line = "someone said 69 @" + str(message.guild)
            # log(line)

    async def baoBRBResponse(self, message):
        # if "brb" in message.content.lower() or "be right back" in message.content.lower() or "afk" in message.content.lower() or "see ya" in message.content.lower() or "see ya later" in message.content.lower() or "see ya ltr" in message.content.lower() or "see you" in message.content.lower() or "see you later" in message.content.lower() or "see you ltr" in message.content.lower() or "see u" in message.content.lower() or "see u later" in message.content.lower() or "see u ltr" in message.content.lower():
            await message.channel.send("bring back some food *squeak*")
            print("somebody went away :(")
            # line = "someone went away @" + str(message.guild)
            # log(line)

    async def baoNomResponse(self, message):
        # if "nomnom" in message.content.lower() or "hungry" in message.content.lower() or "nom" in message.content.lower():
            await message.channel.send(file=discord.File("media/nomnom.gif"))
            print("omnomnom")
            # line = "omnomnom @" + str(message.guild)
            # log(line)

    async def baoPhotoResponse(self, message):  # needs to check every message
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
                comments = ["could be better",
                            "if it had a sunflower seed or a mealworm *squeak* it probably would have received a better rating."]
                comment = random.choice(comments)

            await message.channel.send(str(rating) + "/10 - " + comment)

            print("i rated a pic")
            # line = "i rated a pic @" + str(message.guild)
            # log(line)

    async def baoMentionResponse(self, message):  # needs to check every message
        for i in message.guild.members:
            if i.mentioned_in(message) and not message.mention_everyone:
                await message.channel.send(f"{i.mention} *squeak*  please bring me some food")
