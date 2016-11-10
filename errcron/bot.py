# -*- coding:utf8 -*-
"""Bot class extensions
"""
import datetime
import pytz
from errcron import cronjob


class CrontabMixin(object):
    """Mix-in class to implement crontab features

    If you will use crontab by it, call activate_crontab
    """
    def activate(self):
        super().activate()
        self.activate_crontab()

    def _get_current_time(self):
        if hasattr(self, 'TIMEZONE'):
            # Plugin class has TIMEZONE
            timezone = pytz.timezone(self.TIMEZONE)
            polled_time = datetime.datetime.now(timezone)
        elif hasattr(getattr(self, 'bot_config', None), 'TIMEZONE'):
            # Errbot config has TIMEZONE
            timezone = pytz.timezone(self.bot_config.TIMEZONE)
            polled_time = datetime.datetime.now(timezone)
        else:
            # Use machine timezone
            polled_time = datetime.datetime.now()
        return polled_time

    def activate_crontab(self):
        """Activate polling function and register first crontab
        """
        self._crontab = []
        if hasattr(self, 'CRONTAB'):
            for crontab_spec in self.CRONTAB:
                args = cronjob.parse_crontab(crontab_spec)
                job = cronjob.CronJob()
                if args['_timer'] == 'datetime':
                    job.set_triggers(args['trigger_format'], args['trigger_time'])
                if args['_timer'] == 'crontab':
                    job.set_crontab(args['crontab'])
                if args['action'].startswith('.'):
                    action_name = args['action'][1:]
                    action_ = getattr(self.__class__, action_name)
                else:
                    action_ = args['action']
                job.set_action(action_, *args['args'])
                self._crontab.append(job)
        self.start_poller(30, self.poll_crontab)

    def poll_crontab(self):
        """Check crontab and run target jobs
        """
        polled_time = self._get_current_time()
        if polled_time.second >= 30:
            self.log.debug('Skip cronjobs in {}'.format(polled_time))
            return
        for job in self._crontab:
            if not job.is_runnable(polled_time):
                continue
            job.do_action(self, polled_time)

    def load_job_from_string(self, spec):
        pass
