"""Test case as BotPlugin
"""
from pathlib import Path


pytest_plugins = ['errbot.backends.test']


extra_plugin_dir = str(Path(__file__).parents[1] / 'errcron')


def test_command(testbot):
    testbot.push_message('!crontab_list')
    assert 'List of cronjobs' in testbot.pop_message()
