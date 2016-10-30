import logging

BOT_DATA_DIR = '/var/lib/err'
BOT_EXTRA_PLUGIN_DIR = './'
BOT_LOG_FILE = BOT_DATA_DIR + '/err.log'
BOT_LOG_LEVEL = logging.DEBUG
BOT_LOG_SENTRY = False
SENTRY_DSN = ''
SENTRY_LOGLEVEL = BOT_LOG_LEVEL
BOT_ASYNC = True
BOT_IDENTITY = {
    'username': 'err@localhost',  # The JID of the user you have created for the bot
    'password': 'changeme',       # The corresponding password for this user
}
BOT_ADMINS = ('gbin@localhost',)
CHATROOM_PRESENCE = ('err@conference.server.tld',)
CHATROOM_FN = 'Err'
BOT_PREFIX = '!'
DIVERT_TO_PRIVATE = ()
CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}
