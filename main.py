import logging
import excecoes

from configs.config import *

from discord import Activity, ActivityType
from json import load
from glob import glob
from discord.ext import commands


def command_text(arquivo, comando, text):
    """get the help or brief for a command"""  
    with open('commandtexts.json', 'r', encoding='utf-8') as f:
        data = load(f)
    return data[arquivo][comando][text]
    

def loggermain():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.WARN)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


def main():
    def get_prefix(bot, message):
        with open('data/prefixes.json', 'r') as f:
            arquivo = load(f) 
        prefixo = arquivo[str(message.guild.id)]
        prefixos = [prefixo, SPECIAL_PREFIX]
        return commands.when_mentioned_or(*prefixos)(bot, message) # the server prefix or the special prefix

    bot = commands.Bot(command_prefix=get_prefix, activity=Activity(type=ActivityType.playing, name='Defalt prefix: ..'))


    # load cogs/extentions
    extencoes = glob('cogs\**')
    for extension in extencoes:
        try:
            bot.load_extension(extension.replace('\\','.').replace('.py', ''))
        except Exception as erro:
            print(f'Fail loading extension {extension}: {erro}')


    @bot.event  
    async def on_ready():
        print('**BOT ONLINE!**')


    ################# GLOBAL CHECKS AND BEFORE/AFTER INVOKE #################
    @bot.check_once
    async def black_list(ctx:commands.Context):
        if ctx.message.author.id in BLACK_LIST:
            raise excecoes.OnBlackList()
        return True

    
    @bot.before_invoke
    async def white_list(ctx:commands.Context):
        if ctx.author.id in WHITE_LIST:
            ctx.command.reset_cooldown(ctx)
    #############################################################


    from configs.token import TOKEN
    bot.run(TOKEN)



if __name__ == '__main__':
    loggermain()
    main()