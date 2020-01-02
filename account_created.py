import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
servID = os.getenv('SERVER_ID')

bot = commands.Bot(command_prefix='!')

def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == guild_id
    return commands.check(predicate)

@bot.command()
@commands.is_owner()
@is_in_guild(int(servID))
async def date(ctx, *, member: discord.Member):
    t = member.created_at
    created_time = t.strftime("%#I:%M:%S%p").lower()
    created_date = t.strftime("%B %#d, %Y")            
    date_created = "{} at {} EST".format(created_date, created_time)

    await ctx.send("{}'s account was created on {}".format(member, date_created))

@date.error
async def date_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("you really think we'd let you use this command?")

bot.run(token)