import YUKIIMUSIC.yuki_guard
import config
from YUKIIMUSIC import app
from pyrogram.types import InlineKeyboardButton


def api_btn(text, callback_data=None, url=None, style=None, custom_emoji_id=None):
    if url:
        url_str = str(url)
        if not url_str.startswith("http") and not url_str.startswith("tg://"):
            url_str = f"https://t.me/{url_str.replace('@', '')}"
        btn = InlineKeyboardButton(text=text, url=url_str)
    else:
        btn = InlineKeyboardButton(text=text, callback_data=callback_data)

    if style in ["primary", "danger", "success"]:
        setattr(btn, "style", style)

    if custom_emoji_id:
        setattr(btn, "icon_custom_emoji_id", str(custom_emoji_id))

    return btn


def start_panel(_):
    buttons = [
        [
            api_btn(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style="success",
                custom_emoji_id="5235682785863153026"
            ),
            api_btn(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style="danger",
                custom_emoji_id="5206523956537865948"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    safe_owner_id = config.OWNER_ID[0] if isinstance(config.OWNER_ID, list) else config.OWNER_ID

    buttons = [
        [
            api_btn(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style="success",
                custom_emoji_id="5249244862359812334"
            )
        ],
        [
            api_btn(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style="primary",
                custom_emoji_id="5238162283368035495"
            ),
            api_btn(
                text="˹ 𝚼єʀsιᴏη ˼",
                callback_data="yuki_version_info",
                style="primary",
                custom_emoji_id="5296631769112525274"
            ),
        ],
        [
            api_btn(
                text=_["S_B_6"],
                url=config.SUPPORT_CHANNEL,
                style="primary",
                custom_emoji_id="5253539825360843975"
            ),
            api_btn(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style="danger",
                custom_emoji_id="5258208871423425369"
            ),
        ],
        [
            api_btn(
                text="˹ 𝚼єʙsιᴛє ˼",
                url="https://t.me/+NNVeQYHwW0JlYmM9",
                custom_emoji_id="5262770659267735289"
            ),
        ],
        [
            api_btn(
                text=_["S_B_5"],
                url=f"tg://user?id={safe_owner_id}",
                style="danger",
                custom_emoji_id="5201875852735820002"
            ),
        ],
    ]
    return buttons
