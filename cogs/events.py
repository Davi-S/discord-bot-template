import json

from main import DEFALT_PREFIX
from discord.ext import commands


class EventosCog(commands.Cog, name='Events', description='Catch any event', command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):  # check for all commands in this cog
        return True
    
    async def cog_before_invoke(self, ctx:commands.Context):
        pass

    

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        ################# TO SAVE THE PREFIX #################
        # colect the dict with all prefixes and add the guild and the bot defalt prefix to this dict
        with open('data/prefixes.json', 'r') as f:
            prefixos = json.load(f)

        prefixos[str(guild.id)] = DEFALT_PREFIX

        # rewrite the file with the new guild and prefix
        with open('data/prefixes.json', 'w') as f:
            json.dump(prefixos, f, indent=4)
        ######################################################


        ################# TO KNOW WITH SERVERS THE BOT IS IN #################
        # create the invite
        canais = guild.text_channels
        for _, itb in enumerate(canais):
            try:
                convite = await itb.create_invite()
                break
            except Exception as err:
                continue
            
        with open('data/servers.json', 'r') as f:
            servidores = json.load(f)
        # add to the dict the guild name, an invite, id and a bool that indicates the bot is courently on this server
        servidores[str(guild.name)] = str(convite), str(guild.id), True
        # rewrite the file
        with open('data/servers.json', 'w') as f:
            json.dump(servidores, f, indent=4)
        ######################################################################




    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        ################# TO REMOVE THE PREFIX #################
        with open('data/prefixes.json', 'r') as f:
            prefixos = json.load(f)

        prefixos.pop(str(guild.id))

        with open('data/prefixes.json', 'w') as f:
            json.dump(prefixos, f, indent=4)
        ########################################################


        ################# TO KNOW WITH SERVERS THE BOT IS IN #################
        with open('data/servers.json', 'r') as f:
            servidores = json.load(f)

        # edit the bool to show tha the bot isn't on the server any more
        data = servidores[str(guild.name)]
        data[-1] = False
        servidores[str(guild.name)] = data

        with open('data/servers.json', 'w') as f:
            json.dump(servidores, f, indent=4)
        ######################################################################


def setup(bot):
    bot.add_cog(EventosCog(bot))
    print('Eventos iniciado')