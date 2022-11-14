 # ~ | import discord, so we can actaully code a bot via discord's API.
import discord
from discord.ext import commands
#
#
#
 # ~ | the beginning, we will use this for every future task.
nez = commands.Bot(command_prefix=".", intents=discord.Intents.all()) 
#
#
#
 # -Commands | the bot will respond to your custom commands.
@nez.command()
async def ping(ctx):
    await ctx.send(f"Your Ping: {round(nez.latency * 1000)}ms")
#
@nez.command()
async def hi(ctx):
    await ctx.send("bye")
#
#
#
 # -Logs | the bot will print logs every time someone joins or leaves the server.
@nez.event
async def on_member_join(member):
    print(f"{member} has joined your server")
#
@nez.event
async def on_member_remove(member):
    print(f"{member} has left your server")
#
#
#
 # ~ | the end, hosting
nez.run("")
