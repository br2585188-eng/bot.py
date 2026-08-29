import os
from threading import Thread
import discord
from discord.ext import commands
from flask import Flask

# ==================== KEEP ALIVE WEB SERVER ====================
app = Flask("")


@app.route("/")
def home():
    return "FROST LOUNGE Bot is online 24/7!"


def run_flask():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run_flask)
    t.start()


# ==================== DISCORD BOT SETUP ====================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Configuration IDs
WELCOME_CHANNEL_ID = 1543189838184972298
RULES_CHANNEL_ID = 1543189838184972298
ROLES_CHANNEL_ID = 1539213689847029760
INFO_CHANNEL_ID = 1539213942994501722


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
        file = discord.File("banner.png", filename="banner.png")

        embed = discord.Embed(color=discord.Color.from_rgb(155, 89, 182))

        embed.set_author(
            name=f"Welcome to {member.guild.name} || Hangout • Chilling • Socialize • Gaming",
            icon_url=member.guild.icon.url if member.guild.icon else None,
        )

        embed.title = "__WELCOME TO FROST LOUNGE ™__"
        embed.description = (
            f"╭─ Checkout - <#{RULES_CHANNEL_ID}>\n"
            f"├─ Checkout - <#{ROLES_CHANNEL_ID}>\n"
            f"╰─ Checkout - <#{INFO_CHANNEL_ID}>\n\n"
            f"🐷 have a good journey with us 👼"
        )

        embed.set_image(url="attachment://banner.png")
        top_text = f"HEY {member.mention} **WELCOME** 💖"

        await channel.send(content=top_text, file=file, embed=embed)


# Start Keep-Alive Server & Bot safely via Environment Variable
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
