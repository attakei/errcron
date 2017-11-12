# -*- coding:utf8 -*-
from __future__ import (
    division, print_function, absolute_import, unicode_literals
)
"""cron job structure
"""
import importlib
import types
import six
from crontab import CronTab


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
        self._crontab = None
        self.crontab = None

    def __repr__(self):
        elements = []
        if self.crontab is not None:
            elements.append('crontab=[{}]'.format(self.crontab))
        elif self.trigger_format is None or self.trigger_time is None:
            elements.append('trigger=[]')
        else:
            elements.append('trigger=[{}->{}]'.format(
                self.trigger_format,
                self.trigger_time,
            ))
        return 'CronJob({})'.format(
            ' '.join(elements),
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

    def set_crontab(self, crontab):
        self.crontab = crontab
        self._crontab = CronTab(self.crontab)

    def is_runnable(self, time):
        """Check whether job run action at specified time

        :param time: Time to run action
        :type time: datetime.datetime
        :return: Job is runnable or not
        :rtype: boolean
        """
        if self._crontab is not None:
            # check as 0 second
            zero_time = time.replace(second=0)
            return self._crontab.test(zero_time)
        return time.strftime(self.trigger_format) == self.trigger_time

    def set_action(self, action, *args):
        """Set action and arguments to run in triggered time

        :param action: function path as anction
        :type action: str
        :param args: function arguments
        :type args: list or tuple
        """
        if isinstance(action, (types.FunctionType, types.MethodType)):
            self.action = action
        else:
            action_module = '.'.join(action.split('.')[:-1])
            action_module = importlib.import_module(action_module)
            action = action.split('.')[-1]
            self.action = getattr(action_module, action)
        self.action_args = args

    def do_action(self, plugin, do_time):
        """Run cronjob action with plugin

        :param plugin: running Errbot plugin
        :type plugin: errbot.BotPlugin
        :param do_time: action triggered time
        :type do_time: datetime.datetime
        :return: Returned value from action
        """
        if len(self.action_args) > 0:
            return self.action(plugin, do_time, *self.action_args)
        return self.action(plugin, do_time)


def load_from_string(crontab, format='crontab'):
    """Load cronjob from single string

    :param crontab: crontab string(trigger_format, trigger_time, function, args)
    :type crontab: str
    :param format: job trigger type
    :type format: str
    :return: Cronjob
    :rtype: errcron.cronjob.CronJob
    """
    args = crontab.split()
    job = CronJob()
    if format == 'crontab':
        if args[0].startswith('@'):
            crontab_ = args[0]
            args = args[1:]
            job.set_crontab(crontab_)
        else:
            crontab_ = args[0:5]
            args = args[5:]
            job.set_crontab(' '.join(crontab_))
    elif format == 'datetime':
        trigger_format = args.pop(0)
        trigger_time = args.pop(0)
        job.set_triggers(trigger_format, trigger_time)
    action = args.pop(0)
    job.set_action(action, *args)
    return job


def parse_crontab(crontab):
    args = {}
    splited = crontab.split()
    # Parse time
    if crontab.startswith('%'):
        args['_timer'] = 'datetime'
        args['trigger_format'] = splited.pop(0)
        args['trigger_time'] = splited.pop(0)
    elif crontab.startswith('@'):
        args['_timer'] = 'crontab'
        args['crontab'] = splited.pop(0)
    else:
        args['_timer'] = 'crontab'
        args['crontab'] = ' '.join(splited[0:5])
        splited = splited[5:]
    args['action'] = splited.pop(0)
    args['args'] = splited
    return args
