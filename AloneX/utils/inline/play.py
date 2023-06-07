import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AloneX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    alone = math.floor(percentage)
    if 0 < alone <= 10:
        ba = "⚪─────────"
    elif 10 < alone < 20:
        ba = "━⚪────────"
    elif 20 <= alone < 30:
        ba = "━━⚪───────"
    elif 30 <= alone < 40:
        ba = "━━━⚪──────"
    elif 40 <= alone < 50:
        ba = "━━━━⚪─────"
    elif 50 <= alone < 60:
        ba = "━━━━━⚪────"
    elif 60 <= alone < 70:
        ba = "━━━━━━⚪───"
    elif 70 <= alone < 80:
        ba = "━━━━━━━⚪──"
    elif 80 <= alone < 95:
        ba = "━━━━━━━━⚪─"
    else:
        ba = "━━━━━━━━━⚪"

#bar of alone---------------------------------------
    if 0 < alone <= 1:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 1 <= alone < 2:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 2 <= alone < 3:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 3 <= alone < 4:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 4 <= alone < 5:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 5 <= alone < 6:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 6 <= alone < 7:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 7 <= alone < 8:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 8 <= alone < 9:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 9 <= alone < 10:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 10 <= alone < 11:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 11 <= alone < 12:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 12 <= alone < 13:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢"
    elif 13 <= alone < 14:
        bar = "𝐀ℓσиє 𝐌υѕι¢"
    elif 14 <= alone < 15:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 15 <= alone < 16:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 16 <= alone < 17:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 17 <= alone < 18:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 18 <= alone < 19:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 19 <= alone < 20:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 20 <= alone < 21:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 21 <= alone < 22:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 22 <= alone < 23:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 23 <= alone < 24:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 24 <= alone < 25:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 25 <= alone < 26:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 26 <= alone < 27:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 27 <= alone < 28:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 28 <= alone < 29:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 29 <= alone < 30:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 30 <= alone < 31:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 31 <= alone < 32:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 32 <= alone < 33:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 33 <= alone < 34:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 34 <= alone < 35:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 35 <= alone < 36:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 36 <= alone < 37:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 37 <= alone < 38:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 38 <= alone < 39:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 39 <= alone < 40:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 40 <= alone < 41:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 41 <= alone < 42:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 42 <= alone < 43:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 43 <= alone < 44:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 44 <= alone < 45:
        bar = "𝐀ℓσиє 𝐌υѕι¢"
    elif 45 <= alone < 46:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 46 <= alone < 47:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 47 <= alone < 48:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 48 <= alone < 49:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
    elif 49 <= alone < 50:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 50 <= alone < 51:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 51 <= alone < 52:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 52 <= alone < 53:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 53 <= alone < 54:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 54 <= alone < 55:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 55 <= alone < 56:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 56<= alone < 57:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 57 <= alone < 58:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 58 <= alone < 59:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 59 <= alone < 60:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 60 <= alone < 61:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢"
    elif 61 <= alone < 62:
        bar = "𝐀ℓσиє 𝐌υѕι¢"
    elif 62 <= alone < 63:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 63 <= alone < 64:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 64 <= alone < 65:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 65 <= alone < 66:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 66 <= alone < 67:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 67 <= alone < 68:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 68 <= alone < 69:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 69 <= alone < 70:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 70 <= alone < 71:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 71 <= alone < 72:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 72 <= alone < 73:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 73 <= alone < 74:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 74 <= alone < 75:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 75 <= alone < 76:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 76 <= alone < 77:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 77 <= alone < 78:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 78 <= alone < 79:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 79 <= alone < 80:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 80 <= alone < 81:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 81 <= alone < 82:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 82 <= alone < 83:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 83 <= alone < 84:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 84 <= alone < 85:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 85 <= alone < 86:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 86 <= alone < 87:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 87 <= alone < 88:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 88 <= alone < 89:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 89 <= alone < 90:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 90 <= alone < 91:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 91 <= alone < 92:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 92 <= alone < 93:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 93 <= alone < 94:
        bar = "𝐀ℓσиє 𝐌υѕι¢"
    elif 94 <= alone < 95:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 95 <= alone < 96:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 96 <= alone < 97:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 97 <= alone < 98:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 98 <= alone < 99:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    else:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"


    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{bar}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/ALONE_WAS_BOT"
            ),       
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    alone = math.floor(percentage)
    if 0 < alone <= 10:
        bar = "⚪─────────"
    elif 10 < alone < 20:
        ba = "━⚪────────"
    elif 20 <= alone < 30:
        ba = "━━⚪───────"
    elif 30 <= alone < 40:
        ba = "━━━⚪──────"
    elif 40 <= alone < 50:
        ba = "━━━━⚪─────"
    elif 50 <= alone < 60:
        ba = "━━━━━⚪────"
    elif 60 <= alone < 70:
        ba = "━━━━━━⚪───"
    elif 70 <= alone < 80:
        ba = "━━━━━━━⚪──"
    elif 80 <= alone < 95:
        ba = "━━━━━━━━⚪─"
    else:
        ba = "━━━━━━━━━⚪"

# alone bar-----------------------------------------------------------
    if 0 < alone <= 2:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 2 <= alone < 3:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 3 <= alone < 4:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 4 <= alone < 5:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 5 <= alone < 6:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 6 <= alone < 7:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 7 <= alone < 8:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 8 <= alone < 9:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 9 <= alone < 10:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 10 <= alone < 11:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 11 <= alone < 12:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 12 <= alone < 13:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢"
    elif 13 <= alone < 14:
        bar = "𝐀ℓσиє 𝐌υѕι¢"
    elif 14 <= alone < 15:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 15 <= alone < 16:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 16 <= alone < 17:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 17 <= alone < 18:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 18 <= alone < 19:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 19 <= alone < 20:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 20 <= alone < 21:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 21 <= alone < 22:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 22 <= alone < 23:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 23 <= alone < 24:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 24 <= alone < 25:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 25 <= alone < 26:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 26 <= alone < 27:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 27 <= alone < 28:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 28 <= alone < 29:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 29 <= alone < 30:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 30 <= alone < 31:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 31 <= alone < 32:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 32 <= alone < 33:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 33 <= alone < 34:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 34 <= alone < 35:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 35 <= alone < 36:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 36 <= alone < 37:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 37 <= alone < 38:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 38 <= alone < 39:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 39 <= alone < 40:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 40 <= alone < 41:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 41 <= alone < 42:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 42 <= alone < 43:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 43 <= alone < 44:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 44 <= alone < 45:
        bar = "𝐀ℓσиє 𝐌υѕι¢"
    elif 45 <= alone < 46:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 46 <= alone < 47:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 47 <= alone < 48:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 48 <= alone < 49:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
    elif 49 <= alone < 50:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 50 <= alone < 51:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 51 <= alone < 52:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 52 <= alone < 53:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 53 <= alone < 54:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 54 <= alone < 55:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 55 <= alone < 56:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 56<= alone < 57:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 57 <= alone < 58:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 58 <= alone < 59:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 59 <= alone < 60:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 60 <= alone < 61:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢"
    elif 61 <= alone < 62:
        bar = "𝐀ℓσиє 𝐌υѕι¢"
    elif 62 <= alone < 63:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 63 <= alone < 64:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 64 <= alone < 65:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 65 <= alone < 66:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 66 <= alone < 67:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 67 <= alone < 68:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 68 <= alone < 69:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 69 <= alone < 70:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 70 <= alone < 71:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 71 <= alone < 72:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 72 <= alone < 73:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 73 <= alone < 74:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 74 <= alone < 75:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 75 <= alone < 76:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 76 <= alone < 77:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 77 <= alone < 78:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 78 <= alone < 79:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢"
    elif 79 <= alone < 80:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 80 <= alone < 81:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 81 <= alone < 82:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 82 <= alone < 83:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 83 <= alone < 84:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐒𝗍υᑯ𝗂ⱺ"
    elif 84 <= alone < 85:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 85 <= alone < 86:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 86 <= alone < 87:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 87 <= alone < 88:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 88 <= alone < 89:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 89 <= alone < 90:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 90 <= alone < 91:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐀ℓσиє 𝐌υѕι¢ "
    elif 91 <= alone < 92:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ"
    elif 92 <= alone < 93:
        bar = "𝐀ℓσиє 𝐌υѕι¢ 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 93 <= alone < 94:
        bar = "𝐀ℓσиє 𝐌υѕι¢"
    elif 94 <= alone < 95:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 95 <= alone < 96:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 96 <= alone < 97:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 97 <= alone < 98:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐀ℓσиє 𝐌υѕι¢ 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 98 <= alone < 99:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    else:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{bar}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/ALONE_WAS_BOT"
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐀ℓσиє 𝐌υѕι¢", url=f"https://wynk.in/music")
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/ALONE_WAS_BOT"
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"alonePlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"alonePlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/ALONE_WAS_BOT"
            ),       
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons
