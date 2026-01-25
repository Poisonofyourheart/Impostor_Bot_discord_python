import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intens = discord.Intents.default()
intens.message_content = True
intens.members = True

bot = commands.Bot(command_prefix='$', intents=intens)

@bot.event
async def on_ready():
    print(f'Capitan {bot.user} on duty!')

@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to the server, {member.name}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'hello' in message.content.lower():
        await message.channel.send(f'Hello, {message.author.name}!')
    await bot.process_commands(message)

@bot.command()
async def siema(ctx):
    await ctx.send(f"Siema, {ctx.author.name}!")

@bot.command()
async def droid(ctx):
    rola = discord.utils.get(ctx.guild.roles, name='Droidy')
   
    if rola:
        if rola in ctx.author.roles:
            await ctx.author.remove_roles(rola)
            await ctx.send(f"Nie jesteś już droidem!")
        else:
            await ctx.author.add_roles(rola)
            await ctx.send(f"Jesteś droidem!")
    else:
        await ctx.send("Role 'Droidy' not found.")
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(msg)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)