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

"""
IMPORTANT.
THIS FOLLOWS THE SAME INDEX AS ABOVE. SO INDEX 0 is JACOB, 1 is CARRIGAN.
THE ID's need to correspond with the index.
"""
nickNameID = [246389497053446144,  143040399454240768]


"""
indecees for our arrays so we can refer to people by name
"""
Jacob=0
Carrigan=1
Justin=2
Jackson=3
John=4
LilJoe=5
Chris=6
Joseph=7



"""
Array of commands that take NO paramaters
"""
basicCommands = [ "f!help", "f!hello" ]

"""
Array of commands that take paramaters
"""
advCommands = ["f!penissize"]

####
#   Some notes:
#   for a message object, when referring to the user who sent the message
#   if private channel -> message.user.display_name (this is nickname for the user who sent this object)
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
                 f!size <name> (BRACKETS INCLUDED)
                """.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('f!size'):
        paramType = await detectParamater(message)
        if paramType==2:
            tempName = await scanIDs(message)
            tempName = tempName[:-1]
            paramaterName = '<@' + tempName
           # print(paramaterName)
            #if await detectJacob(message):
             #   size = 10000000000
            #else:
            size = await getSize(message)
            msg = '%s size is about %d inches short!' %(paramaterName + "'s", size)
        elif paramType==1:
            paramaterName = await parseMessageParamaterName(message)
            size = await getSize(message)
            msg = '%s size is about %d inches short!' %(paramaterName + "'s", size)
        else:
            size = await getSize(message)
            msg = '%s size is about %d inches short!' %(message.author.nick + "'s" ,size)
        await client.send_message(message.channel, msg)

    #else:
        #await client.send_message(message.channel, await sys_error(1))

#return a size int. 
async def getSize(m):
    return random.randint(1,8)
"""    
returns an int depending if < or > is detected
0 - No param found
1 - Param found, basic text. i.e., <jacob>
2 - Param found, user ID. i.e., <@Jacob>
"""
async def detectParamater(message):
    found = False
    found2 =False
    spot = 0
    for i in range(len(message.content)):
        if message.content[i] == '<':
            spot = i
            found = True
            break      #TODO, ERROR CHECK NO PARAMS.

    for spot in range(len(message.content)):
        if message.content[spot] == '@':
            idName=True
        if message.content[spot] == '>':
            found2 = True
            break
    
    if found and found2 and idName:
        return 2
    elif found and found2:
        return 1 
    else:
        return 0

async def detectJacob(message):
    temp = message.content.split('!')
    print(temp)
    nameID = temp[2].split('>')
    if int(nameID[0]) == nickNameID[Jacob]:
        return True
    else:
        return False

#this returns a string of paramter name passed in by user with < and > delimiters
async def parseMessageParamaterName(message):
    firstPart = message.content.split('<') #this means index 1 will hold the value "mytext>"
    actualParam = firstPart[1].split('>')
    return actualParam[0]

#When you pass a param with a tag i.e., @Jacob it is actually an ID number. SO we need to get it.
async def scanIDs(message):
    firstPart = message.content.split('@')
    idNum = firstPart[1].split('<')
    return idNum[0]

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
