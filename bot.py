import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

from cogs.greeting import Greeting

bot = commands.Bot(
    # test_guilds=[],
)


# log on_ready
@bot.event
async def on_ready():
    print(f'logged in!')

@bot.slash_command(description="test if the bot is online :)")
async def ping():
    await inter.response.send_message("pong!")


# run the bot
bot.add_cog(Greeting(bot))
bot.run(TOKEN)
