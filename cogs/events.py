import json

from main import DEFALT_PREFIX
from discord.ext import commands



def readjson(arquivo):
    with open(f'{arquivo}.json', 'r', encoding='utf-8') as f:
        pref = json.load(f)
    return pref

def dumpjson(arquivo, data):
    with open(f'{arquivo}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)



class EventosCog(commands.Cog, name='Events', description='Catch any event', command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        ################# TO SAVE THE PREFIX #################
        # colect the dict with all prefixes and add the guild and the bot defalt prefix to this dict
        prefixos = readjson('data/prefixes')

        prefixos[str(guild.id)] = DEFALT_PREFIX

        # rewrite the file with the new guild and prefix
        dumpjson('data/prefixes', prefixos)
        ######################################################

        ################# TO KNOW WITH SERVERS THE BOT IS IN #################
        # try to create an invite until it succeed or there is no more channels to try
        canais = guild.text_channels
        for _, itb in enumerate(canais):
            try:
                convite = await itb.create_invite()
                break
            except Exception as err:
                continue

        servidores = readjson('data/servers')

        # add to the dict the guild name, an invite, id and a bool that indicates the bot is courently on this server
        servidores[str(guild.name)] = str(convite), str(guild.id), True

        # rewrite the file
        dumpjson('data/servers', servidores)
        ######################################################################



    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        ################# TO REMOVE THE PREFIX #################
        prefixos = readjson('data/prefixes')
        prefixos.pop(str(guild.id))
        dumpjson('data/prefixes', prefixos)
        ########################################################

        ################# TO KNOW WITH SERVERS THE BOT IS IN #################
        servidores = readjson('data/servers')

        # edit the bool to show that the bot isn't on the server anymore
        data = servidores[str(guild.name)]
        data[-1] = False
        servidores[str(guild.name)] = data

        dumpjson('data/servers', servidores)
        ######################################################################


def setup(bot):
    bot.add_cog(EventosCog(bot))
    print('Events initiated')

def teardown(bot):
    print('Events unload')