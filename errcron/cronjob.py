# -*- coding:utf8 -*-
"""cron job structure
"""


class CronJob(object):
    def __init__(self):
        self.trigger_time = None
        self.trigger_format = None

    def is_runnable(self, time):
        return time.strftime(self.trigger_format) == self.trigger_time
