from telegram import ChatAction
from haruka.modules.helper_funcs.filters import CustomFilters
import html
import urllib.request
import re
import json
from typing import Optional, List
import time
import urllib
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote_plus, urlencode
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from haruka import dispatcher
from haruka.__main__ import STATS, USER_INFO
from haruka.modules.disable import DisableAbleCommandHandler

def bbs(bot: Bot, update: Update):
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    final = "http://media.oboobs.ru/{}".format(nsfw)
    update.message.reply_photo(final)
		
BOOBS_HANDLER = DisableAbleCommandHandler("lolx", boobs, filters=CustomFilters.sudo_filter)
dispatcher.add_handler(BOOBS_HANDLER)
