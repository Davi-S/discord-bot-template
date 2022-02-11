import excecoes

from discord.ext import commands
from main import command_text, WHITE_LIST

class DevsCog(commands.Cog, name='Devs', description='Commands for devs only', command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot


    async def cog_check(self, ctx):
        # only people on WHITE_LIST can use any command in this cog
        if ctx.author.id not in WHITE_LIST:
            raise excecoes.NotOnWhiteList()
        return True

    async def cog_command_error(self, ctx, erro):
        if isinstance(erro, excecoes.NotOnWhiteList):
            autor = ctx.message.author
            comando = ctx.command
            try:  # warns the author on DM
                await autor.send(f'{ctx.author.mention}, You have no permission to use this command. `{comando.qualified_name}`')

            finally:  # if dm is blocked (or not)
                # warns the author on channel used
                await ctx.send(f'{ctx.author.mention}, This command is only for developers.')

                # notifies the members of the WHITE_LIST
                for member_id in WHITE_LIST:
                    white_member = await self.bot.fetch_user(member_id)
                    await white_member.send(f'{autor} ({ctx.message.author.id}) tried reload an extention: `{comando.qualified_name} {comando.signature}`')



    @commands.command(name='load', aliases=['start', 'carregar', 'iniciar'],
                      help=command_text('developers', 'load', 'help'),
                      brief=command_text('developers', 'load', 'brief'))
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def load(self, ctx, *, cog):
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{ctx.author.mention}, fail loading cog {cog}\nError: {e}')
        else:
            return await ctx.send(f'{ctx.author.mention}, the cog "{cog}" was successfully loaded')


    @commands.command(name='reload', aliases=['restart', 'recarregar', 'reiniciar'],
                      help=command_text('developers', 'reload', 'help'),
                      brief=command_text('developers', 'reload', 'brief'))
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def reload(self, ctx, *, cog):
        try:
            self.bot.reload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{ctx.author.mention}, fail reloading cog {cog}\nError: {e}')
        else:
            return await ctx.send(f'{ctx.author.mention}, the cog "{cog}" was successfully reloaded')


    @commands.command(name='unload', aliases=['unstart', 'descarregar', 'desligar'],
                      help=command_text('developers', 'unload', 'help'),
                      brief=command_text('developers', 'unload', 'brief'))
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unload(self, ctx, *, cog):
        try:
            self.bot.unload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{ctx.author.mention}, fail unloading cog {cog}\nError: {e}')
        else:
            return await ctx.send(f'{ctx.author.mention}, the cog "{cog}" was successfully unloaded')



def setup(bot):
    bot.add_cog(DevsCog(bot))
    print('Devs initiated')

def teardown(bot):
    print('Devs unload')