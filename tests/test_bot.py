# -*- coding:utf8 -*-
from __future__ import (
    division, print_function, absolute_import, unicode_literals
)
from errcron.bot import CrontabMixin


def test_mixin():
    class Impl(CrontabMixin):
        def start_poller(self, interval, func):
            pass

    plugin = Impl()
    plugin.activate_crontab()
    assert hasattr(plugin, '_crontab') is True
    assert isinstance(plugin._crontab, list) is True
