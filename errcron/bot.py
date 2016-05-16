# -*- coding:utf8 -*-
"""Bot class extensions
"""


class CrontabMixin(object):
    """Mix-in class to implement crontab features

    If you will use crontab by it, call activate_crontab
    """
    def activate_crontab(self):
        """Activate polling function and register first crontab
        """
        self._crontab = []

    def poll_crontab(self):
        """Check crontab and run target jobs
        """
        pass
