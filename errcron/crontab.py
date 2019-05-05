from errcron.bot import CrontabMixin
from errbot import BotPlugin, botcmd


class Crontab(CrontabMixin, BotPlugin):
    @botcmd(admin_only=True)
    def crontab_list(self, message, args):
        head = 'List of cronjobs:'
        if len(self._crontab) == 0:
            return f'{head}\n- Not found'
        job_list = [f'- {job}' for job in self._crontab]
        return head + '\n' + '\n'.join(job_list)
