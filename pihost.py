import discord
import os
import random 
import time
from discord.ext import commands

hoster = commands.Bot(command_prefix='.')

@hoster.event 
async def on_ready():
    print('Hoster Is Up')

@hoster.command()
#Create Command
async def create(ctx):
    print('Command Noted')
    await ctx.send('Placeholder')
    os.system('echo LINUX IS GREAT LINUX IS GOD')
    await ctx.send('Linux Integration Complete')
  
    server_number = random.randint(1,5)
    if server_number == 1:
        server_port = 4900
        server_rcon_port = 4910
    elif server_number == 2:
        server_port = 4902
        server_rcon_port = 4912
    elif server_number == 3:
        server_rcon_port = 4913
        server_port = 4903
    elif server_number == 4:
        server_rcon_port = 4914
        server_port = 4904
    else:
        server_rcon_port = 4915
        server_port = 4905

    print(server_number)
    print(server_port)
    await ctx.send('Selecting Server')
    await ctx.send('Deleting Old Worlds')
    os.system(f"rm -r /Server/{server_port}/world*")
    os.system(f"docker start picraft-{server-number}")
    await ctx.send('Server Starting Please wait')
    time.sleep(45)
    await ctx.author.send('Please enter your MC Username for OP')
    await ctx.author.send(f"Server number {server_number}")
    await ctx.author.send(f"Server Address picraft.gq:{server_port} Bedrock is Not supported yet but I will add support very soon!")
    await ctx.send('Please Check DM')
@hoster.command()
async def piversion(ctx):
    print('Version being sent')
    await ctx.send('PiHost Beta 0.4 built by TeraBot452')
@hoster.command()
async def status(ctx):
    print('Giving Status')
    await ctx.send('Currently All Commands Are Placeholders.')
@hoster.event
async def on_message(message):
    if message.guild is None and str(message.author) !="PiHost-Test#9609":
            name = (message.content)
            os.system(f'mcrcon -P {server_rcon_port} -p minecraft -w 1 "op {name}"')
            await message.author.send("Enjoy Your Server.  It will stop in about 6 hours.  For more permanent hosting, DM me")


        
    #Below is the line that makes commands and messages work 
    await hoster.process_commands(message)



hoster.run('ODQ0MTkxMDM1NzMwMjk2ODUz.YKO0Kw.mxZCSjfb9PXtQVEVaTezgqxFjUs')

#Things to do
#Incoorperate Docker.py instead of docker cli
#Add a system to make sure that numbers do not get reused if the server is active (Most likely a plugin)
#Download and Upload worlds. (Maybe a website?? Or FTP maybe)
#Database of plugins
#Try to replace rcon with docker.  Or Replace the docker containers with screen
