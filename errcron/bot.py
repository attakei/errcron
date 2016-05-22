# -*- coding:utf8 -*-
"""Bot class extensions
"""
import datetime
from errcron import cronjob


class CrontabMixin(object):
    """Mix-in class to implement crontab features

    If you will use crontab by it, call activate_crontab
    """
    def activate_crontab(self):
        """Activate polling function and register first crontab
        """
        self._crontab = []
        if hasattr(self, 'CRONTAB'):
            for crontab_spec in self.CRONTAB:
                job = cronjob.load_from_string(crontab_spec)
                self._crontab.append(job)
        self.start_poller(60, self.poll_crontab)

    def poll_crontab(self):
        """Check crontab and run target jobs
        """
        polled_time = datetime.datetime.now()
        for job in self._crontab:
            if not job.is_runnable(polled_time):
                continue
            job.do_action(self, polled_time)
