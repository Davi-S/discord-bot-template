from discord.ext import commands

from excecoes import NotOnWhiteList, OnBlackList


class ErrosCog(commands.Cog, name='Errors', description='Catch any errors', command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, erro):
        if isinstance(erro, NotOnWhiteList):
            return  # NotOnWhiteList error are beeing treated on the developers cog

        if isinstance(erro, OnBlackList):
            return await ctx.send(f'{ctx.author.mention}, you are on the BlackList and can not '
                                    'use any bot command.\nPlease contact a developer')
        
        await ctx.send(f'{ctx.author.mention}, {erro}')
        


def setup(bot):
    bot.add_cog(ErrosCog(bot))
    print('Errors initiated')

def teardown(bot):
    print('Errors unload')