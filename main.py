import discord
from datetime import datetime
# from logger import Logger
import logging
from hamster import Hamster

client = discord.Client()
# logger = Logger()
hamster = Hamster(10, 10, 10)

today = "logs/" + datetime.today().strftime(('%d-%m-%Y')) + ".txt"

logging.basicConfig(
    level = logging.INFO,
    format= '%(time) %(message)s',
    filename = today
)
# def log(line):
#     time = datetime.today().strftime('%H:%M:%S | ')
#     f = open(today, 'a')
#     f.write(time + line)
#     f.write("\n")
#     f.close()


@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    FORMAT =
    d = {'time': datetime.today().strftime("%H:%M:%S | ")}
    logging.basicConfig(filename=today, format=FORMAT)
    logging.info("'Successfully logged in as {0.user}'.format(client)", extra=d)
    # f = open(today, 'a')
    # f.write("Successfully initialised at " + datetime.today().strftime('%H:%M:%S'))
    # f.write("\n")
    # f.close()


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if channel == member.guild.system_channel:
            await channel.send("*squeaks sadly*  someone left the server :'( i hope they come back and bring me sunflower seeds")
    print(str(member) + " left " + str(member.guild))
    # line = str(member) + " left " + str(member.guild)
    # log(line)


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel == member.guild.system_channel:
            await channel.send(f"*squeak*  welcome to SADCATZ, {member.mention}! give me mealworms and/or sunflower seeds and i will love you forever :heart: \n\n*call my name and i'll probably squeak at you*")
    print(str(member) + " joined " + str(member.guild))
    # line = str(member) + " joined " + str(member.guild)
    # log(line)


@client.event
async def on_message(message):
    if message.author == client.user:  # does not reply to bots, including itself
        return
    else:
        await hamster.msgResponse(message)


f = open("token.txt", "r")
token = f.read()
client.run(token)
