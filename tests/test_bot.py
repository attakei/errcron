# -*- coding:utf8 -*-
from __future__ import (
    division, print_function, absolute_import, unicode_literals
)
from freezegun import freeze_time
from errcron.bot import CrontabMixin
from errcron.cronjob import CronJob


class MockedImpl(CrontabMixin):
    def start_poller(self, interval, func):
        pass


def test_mixin():
    plugin = MockedImpl()
    plugin.activate_crontab()
    assert hasattr(plugin, '_crontab') is True
    assert isinstance(plugin._crontab, list) is True


def test_polled_once(capsys):
    job1 = CronJob()
    job1.set_action('stub.print_datetime', 'sample')
    job1.set_triggers('%H', '00')
    job2 = CronJob()
    job2.set_action('stub.print_datetime', 'sample')
    job2.set_triggers('%H', '01')

    plugin = MockedImpl()
    plugin._crontab = [job1, job2, ]
    with freeze_time('2016-01-01 00:00:01'):
        plugin.poll_crontab()
        out, err = capsys.readouterr()
        assert out == '2016-01-01'