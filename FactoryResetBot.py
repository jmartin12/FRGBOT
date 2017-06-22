"""
Factory Reset Games bot.
Created by KJ
6/22/17
Doing the LAWDS work
"""
import random
import discord
import logging

"""
Logging errors to file dicord.log
levels of errors are: crititcal, error, warning, info, and debug
defualt is warning
"""

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)


"""
token ID from discords website
"""
token = 'MzI3MTcxOTA2Njk4NzM5NzE0.DC1Stw.8Lb7TqRTnvuqw5u5aiAR4ke-Pn4'

"""
server ID, as of now its my testBotServer
"""
serverID = 327436572175630349


"""
Client object to communicate to a server with a bot
"""
client = discord.Client()

"""
random seed generated only once
"""
random.seed()

"""
me :)
"""
theProphet = "Jacob"


"""
Array of nicknames in our server.
"""
nickNames = [ theProphet, "Carrigan", "RIOT MARTINJSTN1", "Jackson", "grand maester simpson", "Joe W", "Chris L", "Joseph" ]


####
#   Some notes:
#   for a message object, when referring to the user who sent the message
#   if private channel -> message.user.display_name (this is nickname for this object)
#   if public channel -> message.author.nick
####


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('f!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('f!help'):
        msg = """ Welcome to the Factory Reset Games Bot! \n
                Issue commands with f! \n
                List of available commands: \n
                 f!help
                 f!hello
                 f!penissize <name> (BRACKETS INCLUDED)
                """.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('f!penissize'):
        await detectParamater(message)
        size = await getPenisSize(message)
        msg = '%s penis size is about %d inches short' %(message.author.nick ,size)
        await client.send_message(message.channel, msg)

    else:
        await client.send_message(message.channel, sys_error(1))

#return a penis size int. 
async def getPenisSize(m):
    print(m.content)
    if m.channel.is_private:
        if m.user.display_name == theProphet:
            return 1000000000
        else:
            return random.randint(1,8)
    else:
        if m.author.nick == theProphet:
            return 100000000
        else:
            print(m.author.nick)
            return random.randint(1,8)
    

#returns the first paramater with delimeters '<' '>'
async def detectParamater(message):
    found = False
    spot = 0
    for i in range(len(message.content)):
        if message.content[i] == '<':
            spot = i
            found = True
            break      #TODO, ERROR CHECK NO PARAMS.
    if found:
        originalParamaterName = await parseMessageParamaterName(i, message)
    else:
        return -1

#this returns a string of paramter name passed in by < and > delimiters
async def parseMessageParamaterName(index, message): #TODO, errorcheck no >
    cont = True
    name = ""
    #TODO parse up until > then return


async def sys_error(num):
    if num == 1:
        return "Invalid syntax! type f!help for more information"

@client.event
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('-----------')

client.run(token)
