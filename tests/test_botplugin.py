"""Test case as BotPlugin
"""
from pathlib import Path

import pytest

from errcron.cronjob import CronJob
from errcron.crontab import Crontab


pytest_plugins = ['errbot.backends.test']

extra_plugin_dir = str(Path(__file__).parents[1] / 'errcron')

extra_config = {
    'BOT_ADMINS': ('admin', )
}


@pytest.mark.parametrize('sender,expect', [
    ('user', 'This command requires bot-admin privileges'),
    ('admin', 'List of cronjobs:\n- Not found'),
])
def test_list_is_admin_only(sender, expect, testbot):
    testbot.bot.sender = testbot.bot.build_identifier(sender)
    testbot.push_message('!crontab_list')
    assert  expect == testbot.pop_message()


def test_list_jobs(testbot):
    plugin: Crontab = testbot._bot.plugin_manager.get_plugin_obj_by_name('Crontab')
    plugin._crontab.append(CronJob())
    testbot.bot.sender = testbot.bot.build_identifier('admin')
    testbot.push_message('!crontab_list')
    actual = testbot.pop_message()
    expect = 'List of cronjobs:\n'
    assert expect in actual
    assert len(actual.split('\n')) == 2
    assert 'CronJob(trigger=[])' in actual
