import disnake
from disnake.ext import commands

import os
import pickle

"""
class for greeting commands:
 - announce member join, leave, kick, ban
 - random messages for each of them
 - replace mentions/usernames in announcement messages
 - set channel to announce in ✅
 - set messages
 - save and load the messages/channel to data.json
"""



class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data = {
            "channel": None,
            "welcome": [],
            "goodbye": [],
            "kick": [],
            "ban": []
        }

    # parent command (for subcommands)
    @commands.slash_command()
    async def greeting(inter, *args):
        pass

    # test greet
    @greeting.sub_command(name="test", description="test command")
    async def greeting_test(self, ctx):
        await self.on_member_join(ctx.author)
        await ctx.response.send_message("sent!")


    # member join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.data["channel"]

        if channel is not None:
            await channel.send(f'welcome, {member.mention}!')


    # set channel to send greetings in
    @greeting.sub_command(name="channel", description="choose a channel to welcome new members in")
    async def greeting_channel(self, ctx, channel: disnake.abc.GuildChannel):
        self.data["channel"] = channel
        await ctx.response.send_message("greeting channel set to " + channel.mention + ".")
