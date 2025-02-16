import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '935917386').split()]
USERNAME = environ.get('USERNAME', "")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002382706496'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', '')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
PICS = (environ.get('PICS', '')).split()
START_IMG = environ.get('START_IMG', '')
NOR_IMG = environ.get('NOR_IMG', "")
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', ''))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1001939828492'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002440956285'))
URL = environ.get('URL', 'mytestbot-jvdfhbj.com')
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '150'))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "okay")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'films')

LANGUAGES = ["malayalam", "english", "tamil", "hindi", "telugu", "kannada", "Multi Audio", "Dual Audio"]
QUALITIES = ["HDRip","WEBDL" ,"BluRay", "WEBRip", "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k"]
YEARS = [f'{i}' for i in range(2025 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
request_channel = environ.get('REQUEST_CHANNEL', '-1002393842854')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002393842854'))
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', True)
POST_CHANNELS = list(map(int, (channel.strip() for channel in environ.get('POST_CHANNELS', '-1002393842854').split(','))))

#Auto Approve 
APICS = (environ.get('APICS', '')).split()
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", f"{script.APPROVED_TEXT}")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '7'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 250))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', False)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'imdb': IMDB,
            'link': LINK_MODE
    }
