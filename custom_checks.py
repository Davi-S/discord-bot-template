from main import SPECIAL_PREFIX, WHITE_LIST
from discord.ext import commands



# this decorator acts like a 'has_permissions' decorator for functions, but returns True is the special prefix was used and the autor is on white_list
def specialprefix_or_permissions(**perms):        
    has_perms = commands.has_permissions(**perms).predicate 
    async def extended_check(ctx):
        if (ctx.author.id in WHITE_LIST) and (ctx.prefix == SPECIAL_PREFIX):
            await ctx.send(f'{ctx.author.mention}, COMMAND USED ON MASTER MODE')
            return True  # true for this check if I use the special prefix

        if not await has_perms(ctx): 
            raise commands.errors.MissingPermissions(list(perms.keys()))
        else:
            return True 
    return commands.check(extended_check)