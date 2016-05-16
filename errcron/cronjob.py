# -*- coding:utf8 -*-
from __future__ import (
    division, print_function, absolute_import, unicode_literals
)
"""cron job structure
"""
import importlib
import six


class CronJob(object):
    """Job runner for errcron, handling job running trigger and action
    """
    def __init__(self):
        self.trigger_format = None
        """datetime format by trigger to run job"""
        self.trigger_time = None
        """datetime value by trigger to run job"""
        self.action = None
        """Job action"""

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
        """Set trigger_format and trigger_time (recommend)

        :param trigger_format: datetime format used by strftime
        :type trigger_format: basestring
        :param trigger_format: datetime values returned by strftime
        :type trigger_time: basestring
        :raises: ValueError
        """
        if not isinstance(trigger_format, six.string_types):
            raise ValueError
        if not isinstance(trigger_time, six.string_types):
            raise ValueError
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

    def set_action(self, action, *args):
        action_module = '.'.join(action.split('.')[:-1])
        action_module = importlib.import_module(action_module)
        action = action.split('.')[-1]
        self.action = getattr(action_module, action)
        self.action_args = args

    def do_action(self, do_time):
        return self.action(do_time, *self.action_args)
