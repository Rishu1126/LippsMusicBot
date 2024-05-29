import math

from pyrogram.types import InlineKeyboardButton

from LippsMusic.utils.formatters import time_to_seconds


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


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "𝐘𝐨𝐮𝐭 𝐒𝐨𝐧𝐠 𝐢𝐬 𝐩𝐥𝐚𝐲𝐢𝐧𝐠 💟"
    elif 10 < umm < 20:
        bar = "𝐉𝐨𝐢𝐧 𝐨𝐮𝐫 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩"
    elif 20 <= umm < 30:
        bar = "𝐅𝐨𝐫 𝐦𝐨𝐫𝐞 𝐮𝐩𝐝𝐚𝐭𝐞 💗"
    elif 30 <= umm < 40:
        bar = "𝐨𝐰𝐧𝐞𝐫 𝐨𝐟 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 𝐢𝐬 𝐘𝐚𝐬𝐡𝐮"
    elif 40 <= umm < 50:
        bar = "𝐜𝐫𝐞𝐚𝐭𝐨𝐫 𝐨𝐟 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 𝐢𝐬 𝐀𝐛𝐡𝐢𝐬𝐡𝐞𝐤"
    elif 50 <= umm < 60:
        bar = "𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚𝐧 𝐀𝐧𝐭𝐢𝐥𝐚𝐠"
    elif 60 <= umm < 70:
        bar = "𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 💗"
    elif 70 <= umm < 80:
        bar = "𝐚𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 💗 "
    elif 80 <= umm < 95:
        bar = "𝐟𝐨𝐫 𝐚𝐧𝐲 𝐐𝐮𝐞𝐫𝐲"
    else:
        bar = "𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐨 @abhi_rss 💗"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="𝐎𝐰𝐧𝐞𝐫 🥂", url=f"https://t.me/Yashuwinee"),
            InlineKeyboardButton(text="𝐃𝐄𝐕 💗" , url=f"https://t.me/Abhi_rss"),
            InlineKeyboardButton(text="𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐀𝐓 🧿", url=f"https://t.me/TheShitChat"),
            InlineKeyboardButton(text="𝐔𝐏𝐃𝐀𝐓𝐄 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ⚠️", url=f"https://t.me/hpandazzzworld"),
            InlineKeyboardButton(text="𝐅𝐨𝐫 𝐋𝐚𝐭𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 🎥", url=f"https://t.me/Trending_Era"),            
        ],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="𝐎𝐰𝐧𝐞𝐫 🥂", url=f"https://t.me/Yashuwinee"),
            InlineKeyboardButton(text="𝐃𝐄𝐕 💗" , url=f"https://t.me/Abhi_rss"),
            InlineKeyboardButton(text="𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐀𝐓 🧿", url=f"https://t.me/TheShitChat"),
            InlineKeyboardButton(text="𝐔𝐏𝐃𝐀𝐓𝐄 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ⚠️", url=f"https://t.me/hpandazzzworld"),
            InlineKeyboardButton(text="𝐅𝐨𝐫 𝐋𝐚𝐭𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 🎥", url=f"https://t.me/Trending_Era"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="𝐇𝐢𝐝𝐞 𝐦𝐞 🌝")],
    ]
    return buttons 
