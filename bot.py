import os
import discord
from discord.ext import commands

# Bot Intents Setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ==================== CONFIGURATION ====================
WELCOME_CHANNEL_ID = 1543189838184972298  # Welcome Channel ID
RULES_CHANNEL_ID = 1543189838184972298    # Rules Channel ID
ROLES_CHANNEL_ID = 1539213689847029760    # Self-Roles Channel ID
INFO_CHANNEL_ID = 1539213942994501722     # Announcement / Info Channel ID

IMAGE_FILE = "banner.gif"
# ========================================================

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - Frost.gg Active! ❄️")
    await bot.change_presence(
        activity=discord.Game(name="FROST LOUNGE ™ | !help")
    )

@bot.event
async def on_member_join(member):
    print(f"Member joined: {member.name}")

    try:
        channel = await bot.fetch_channel(WELCOME_CHANNEL_ID)
    except Exception as e:
        print(f"Channel fetch error: {e}")
        return

    if channel:
        # Local Image Attachment Setup (banner.gif)
        file = discord.File(IMAGE_FILE, filename=IMAGE_FILE)

        # Main Embed Setup
        embed = discord.Embed(color=discord.Color.from_rgb(155, 89, 182))
        
        # Author Header
        embed.set_author(
            name=f"Welcome to {member.guild.name} || Hangout • Chilling • Socialize • Gaming",
            icon_url=member.guild.icon.url if member.guild.icon else None
        )

        # Title & Bullet Points
        embed.title = "__WELCOME TO FROST LOUNGE ™__"
        embed.description = (
            f"╭─ Checkout - <#{RULES_CHANNEL_ID}>\n"
            f"├─ Checkout - <#{ROLES_CHANNEL_ID}>\n"
            f"╰─ Checkout - <#{INFO_CHANNEL_ID}>\n\n"
            f"🐷 have a good journey with us 👼"
        )

        # Attach image dynamically
        embed.set_image(url=f"attachment://{IMAGE_FILE}")

        # Mention Header Text
        top_text = f"HEY {member.mention} **WELCOME** 💖"

        # Send message
        await channel.send(content=top_text, file=file, embed=embed)

# Render Environment Variable se Token automatic pull karne ke liye
bot.run(os.getenv("DISCORD_TOKEN"))
