import discord
from discord.ext import commands
from main import MY_COLOR, PREFIX #we're using our main colour & prefix that we declared in our main.py file

#this is how to set up a basic cog

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot #you can assign more self variables here if you want

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000,1)
        await ctx.send(f"Pong! {latency}ms")

    @commands.command(aliases=["commands"])
    async def help(self, ctx):
        embed = discord.Embed(title="Commands", description="These are my available commands!", color=MY_COLOR)
        # embed.set_author(name="Template Bot", icon_url="https://imgur.com/youricon.png")
        # embed.set_thumbnail(url="https://imgur.com/yourthumbnail.png")
        embed.add_field(name=PREFIX + "ping", value="Returns the bot latency", inline=False) #if you don't want your embed key:values on seperate lines, remove inline=False
        embed.add_field(name=PREFIX + "help", value="Returns this help box", inline=False)
        embed.set_footer(text="P.S. star my repo after using this template!")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))
