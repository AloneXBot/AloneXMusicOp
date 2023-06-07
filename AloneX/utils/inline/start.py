from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᑯᑯ 𝐀ℓσиє 𝐌υѕι¢ 𝚰𐓣 𝐆𝗋ⱺυρ ",
                url=f"https://t.me/JiosaavnTetrisbot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝒆𝒍𝒑",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝑺𝒆𝒕𝒕𝒊𝒏𝒈𝒔", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᑯᑯ 𝐀ℓσиє 𝐌υѕι¢ 𝚰𐓣 𝐆𝗋ⱺυρ",
                url=f"https://t.me/JiosaavnTetrisbot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝒆𝒍𝒑", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="𝐀ℓσиє 𝐌υѕι¢", url=f"https://www.spotify.com/"
            )
        ],
     ]
    return buttons

