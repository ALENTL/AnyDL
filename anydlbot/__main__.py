#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ALEN TL

# the logging things
from anydlbot import API_HASH, APP_ID, DOWNLOAD_LOCATION, TG_BOT_TOKEN
from pyrogram import Client
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)


logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    plugins = dict(
        root="anydlbot/plugins"
    )
    app = Client(
        "AnyDLBot",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.set_parse_mode("html")
    app.run()