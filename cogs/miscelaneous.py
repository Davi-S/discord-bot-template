from discord.ext import commands
from main import command_text

class DiversosCog(commands.Cog, name='Misc', description='Commands that do not fit any other Cog'):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='ping',
                      help=command_text('miscelaneous', 'ping', 'help'),
                      brief=command_text('miscelaneous', 'ping', 'brief'))
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send('Pong!')
        

    @commands.command(name='pong',
                      help=command_text('miscelaneous', 'pong', 'help'),
                      brief=command_text('miscelaneous', 'pong', 'brief'))
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pong(self, ctx):
        await ctx.send('Ping!')
    

def setup(bot):
    bot.add_cog(DiversosCog(bot))
    print('Misc initiated')

def teardown(bot):
    print('Misc unload')