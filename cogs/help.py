import discord
from discord.ext import commands

# minimal help from discord
class MinimalHelp(commands.MinimalHelpCommand):
    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error)
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)


# customizable help
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

    async def on_help_command_error(self, ctx, error):
        return await super().on_help_command_error(ctx, error)
    
    async def send_error_message(self, error):
        return await super().send_error_message(error)



class HelpCogs(commands.Cog):
    def __init__(self, bot):
       self.bot = bot

       # Setting the cog for the help
       help_command = MinimalHelp()  # Using minimal help, but custom help could be used if you want
       help_command.cog = self  # Instance of YourCog class
       bot.help_command = help_command


def setup(bot):
    bot.add_cog(HelpCogs(bot))
    print('Help initiated')

def teardown(bot):
    print('Help unload')