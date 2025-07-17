import discord
from discord.ext import commands

TOKEN = "TON_TOKEN"
GUILD_ID = 123456789
ROLE_ID = 987654321

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

async def give_role(discord_id):
    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(discord_id)
    role = guild.get_role(ROLE_ID)
    await member.add_roles(role)