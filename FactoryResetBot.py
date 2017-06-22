"""
Factory Reset Games bot.
Created by KJ
6/22/17
Doing the LAWDS work
"""

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


client = discord.Client()




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('f!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('f!help'):
        msg = """ Welcome to the Factory Reset Games Bot! \n
                Issue command with f! \n
                List of available command: \n
                 f!help
                 f!hello
                """.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('-----------')

client.run(token)
