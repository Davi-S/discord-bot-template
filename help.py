import discord
from discord.ext import commands


class MinimalHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)


class CustomHelp(commands.HelpCommand):
    def _init_(self):
        super().__init__()


    async def send_bot_help(self, mapping):
        return await super().send_bot_help(mapping)
        
    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)

    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        return await super ().send_command_help(command)