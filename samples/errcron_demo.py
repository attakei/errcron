from errbot import BotPlugin
from errcron import CrontabMixin


class ErrcronDemo(CrontabMixin, BotPlugin):
    """
    Demo for errcron
    """
    CRONTAB = [
        '* * * * * .notify_minute @attakei',
    ]

    def notify_minute(self, polled_time, identity):
        user = self.build_identifier(identity)
        return self.send(user, 'Currently {}'.format(polled_time.strftime('%H:%M')))
