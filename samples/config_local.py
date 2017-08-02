import logging
import os


BASE_DIR = os.path.dirname(__file__)

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Text'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = os.path.join(BASE_DIR, r'data')
BOT_EXTRA_PLUGIN_DIR = BASE_DIR

BOT_LOG_FILE = os.path.join(BASE_DIR, r'errbot.log')
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@attakei', )  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!
BOT_IDENTITY = {
    'username': '@attakei',
    'password': 'changeme',
}
