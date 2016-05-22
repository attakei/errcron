# -*- coding:utf8 -*-
"""Bot actions
"""


def post_message(plugin, polled_time, identity, message):
    """Post single message

    :type plugin: errbot.BotPlugin
    :type polled_time: datetime.datetime
    :type identity: str
    :type message: str
    """
    user = plugin.build_identifier(identity)
    return plugin.send(user, message)
