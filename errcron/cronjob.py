# -*- coding:utf8 -*-
"""cron job structure
"""


class CronJob(object):
    """Job runner for errcron, handling job running trigger and action
    """
    def __init__(self):
        self.trigger_format = None
        """datetime format by trigger to run job"""
        self.trigger_time = None
        """datetime value by trigger to run job"""

    def __repr__(self):
        if self.trigger_format is None or self.trigger_time is None:
            trigger_str = ''
        else:
            trigger_str = '{}->{}'.format(
                self.trigger_format,
                self.trigger_time,
            )
        return 'CronJob(trigger=[{}])'.format(
            trigger_str,
        )

    def set_triggers(self, trigger_format, trigger_time):
        self.trigger_format = trigger_format
        self.trigger_time = trigger_time

    def is_runnable(self, time):
        """Check whether job run action at specified time

        :param time: Time to run action
        :type time: datetime.datetime
        :return: Job is runnable or not
        :rtype: boolean
        """
        return time.strftime(self.trigger_format) == self.trigger_time
