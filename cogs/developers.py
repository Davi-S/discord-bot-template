from discord.ext import commands
from main import command_text, WHITE_LIST

class DevsCog(commands.Cog, name='Devs', description='Commands for devs only', command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot


    async def cog_check(self, ctx):
        return True
    
    async def cog_before_invoke(self, ctx:commands.Context):
        pass



    @commands.command(name='reload', aliases=['restart', 'recarregar', 'reiniciar'],
                      help=command_text('developers', 'reload', 'help'),
                      brief=command_text('developers', 'reload', 'brief'))
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def reload(self, ctx, cog):
        if ctx.message.author.id in WHITE_LIST:
            self.bot.reload_extension(f'cogs.{cog}')
            return await ctx.send(f'{ctx.author.mention}, the cog "{cog}" was successfully reloaded')
        
        else:
            autor = ctx.message.author
            comando = self.bot.get_command('reload')
            try:  # warns the author on DM
                await autor.send(f'{ctx.author.mention}, You have no permission to use this command. `{comando.qualified_name}`.')

            
            finally:  # if dm is blocked (or not)
                autor_id = ctx.message.author.id

                # warns the author on channel used
                await ctx.send(f'{ctx.author.mention}, This command is only for developers.')

                # notifies the members of the WHITE_LIST
                for member_id in WHITE_LIST:
                    white_member = await self.bot.fetch_user(member_id)
                    await white_member.send(f'{autor} ({autor_id}) tried reload an extention ({cog}): '
                                            f'`{comando.qualified_name} {comando.signature}`')



def setup(bot):
    bot.add_cog(DevsCog(bot))
    print('Devs iniciado')