from errbot import BotPlugin, botcmd


class Crontab(BotPlugin):
    @botcmd
    def crontab_list(self, message, args):
        return 'List of cronjobs'
