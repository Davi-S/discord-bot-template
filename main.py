from configs.config import *

from discord import Activity, ActivityType
from json import load
from glob import glob
from discord.ext import commands


def command_text(arquivo, comando, text):
    with open('commandtexts.json', 'r') as f:
        data = load(f)
    return data[arquivo][comando][text]
    

def main():
    def get_prefix(bot, message):
        with open('data/prefixes.json', 'r') as f:
            arquivo = load(f) 
        prefixo = arquivo[str(message.guild.id)]
        prefixos = [prefixo, SPECIAL_PREFIX]
        return commands.when_mentioned_or(*prefixos)(bot, message) # the server prefix or the special prefix

    bot = commands.Bot(command_prefix=get_prefix, activity=Activity(type=ActivityType.playing, name='defalt prefix: ..'))

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
    def check_commands(ctx):
        return True


    @bot.check_once
    async def black_list(ctx:commands.Context):
        if ctx.message.author.id in BLACK_LIST:
            await ctx.send(f'{ctx.author.mention}, You are on BLACK_LIST and can not use any command')
            #TODO make a custom error for black list
            return False
        return True

    
    @bot.before_invoke
    async def white_list(ctx:commands.Context):
        if ctx.author.id in WHITE_LIST:
            ctx.command.reset_cooldown(ctx)


    @bot.after_invoke
    async def after(ctx:commands.Context):
        pass
    #############################################################


    from configs.token import TOKEN
    bot.run(TOKEN)



if __name__ == '__main__':
    main()