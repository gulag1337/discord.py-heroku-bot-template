import discord
import os
import asyncio
import sys
import traceback
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN") #you must add a Config Vars in your Heroku app settings (Format - KEY:DISCORD_TOKEN, VALUE: your token)
PREFIX = "$" #set your prefix here
MY_COLOR = discord.Color.from_rgb(142, 224, 243) #set your main discord bot colour (for embeds, etc) here

intents = discord.Intents().all() #only if you want to use all Privileged Gateway intents. Note : you must enable this on your dev portal (https://discord.com/developers/applications)!
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command("help") #Removes the default help command, so you can set a custom one

@bot.command(aliases=["loadcog"]) #example of how to set another name for this command : $loadcog will do the same thing as $load
@commands.is_owner() #only runs if the bot owner calls this command
async def load(ctx, cog):
    try:
        bot.load_extension(f"cogs.{cog}")
        await ctx.message.add_reaction('☑️')
    except:
        await ctx.send('**Error :**\n```py\n%s\n```' % traceback.format_exc())


@bot.command()
@commands.is_owner()
async def unload(ctx, cog):
    try:
        bot.unload_extension(f"cogs.{cog}")
        await ctx.message.add_reaction('☑️')
    except:
        await ctx.send('**Error :**\n```py\n%s\n```' % traceback.format_exc())
        
@bot.command()
@commands.is_owner()
async def reload(ctx, cog):
    try:
        bot.reload_extension(f"cogs.{cog}")
        await ctx.message.add_reaction('☑️')
    except:
        await ctx.send('**Error :**\n```py\n%s\n```' % traceback.format_exc())

for filename in os.listdir("./cogs"): #loads the cog files located in the cogs folder
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)
