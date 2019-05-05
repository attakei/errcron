from errcron.bot import CrontabMixin
from errbot import BotPlugin, botcmd


class Crontab(CrontabMixin, BotPlugin):
    @botcmd(admin_only=True)
    def crontab_list(self, message, args):
        return 'List of cronjobs'
