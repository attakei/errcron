"""Test case as BotPlugin
"""
from pathlib import Path

import pytest

pytest_plugins = ['errbot.backends.test']

extra_plugin_dir = str(Path(__file__).parents[1] / 'errcron')

extra_config = {
    'BOT_ADMINS': ('admin', )
}


@pytest.mark.parametrize('sender,expect', [
    ('user', 'This command requires bot-admin privileges'),
    ('admin', 'List of cronjobs'),
])
def test_list_is_admin_only(sender, expect, testbot):
    testbot.bot.sender = testbot.bot.build_identifier(sender)
    testbot.push_message('!crontab_list')
    assert  expect == testbot.pop_message()
