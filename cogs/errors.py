from discord.ext import commands


class ErrosCog(commands.Cog, name='Errors', description='Catch any errors', command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):  # check for all commands in this cog
        return True
    
    async def cog_before_invoke(self, ctx:commands.Context):
        pass

    
    @commands.Cog.listener()
    async def on_error(self, event):
        print(event)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, erro):
        await ctx.send(f'{ctx.author.mention}, {erro}, {type(erro)}')
        


def setup(bot):
    bot.add_cog(ErrosCog(bot))
    print('Erros iniciado')