from discord.ext import commands


class CustomErrors(commands.CommandError):
    pass


class NotOnWhiteList(CustomErrors):
    def __init__(self, message:str='Not on the WhiteList', *args):
        if message is not None:
            # clean-up @everyone and @here mentions
            m = message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            super().__init__(m, *args)
        else:
            super().__init__(*args)



class OnBlackList(CustomErrors):
    def __init__(self, message:str='On BlackList', *args):
        if message is not None:
            # clean-up @everyone and @here mentions
            m = message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            super().__init__(m, *args)
        else:
            super().__init__(*args)