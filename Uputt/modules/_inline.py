import random
import re

from telethon import Button
from telethon.sync import custom, events
from telethon.tl.types import InputWebDocument

from config import var
from Uputt import Uputt, CMD_HELP, bot, ibuild_keyboard, paginate_help
from Uputt.iamuput import HOSTED_ON


BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
main_help_button = [
    [
        Button.inline("•• Mᴇɴᴜ ••", data="reopen")],
]
logouputt = random.choice(
    [
        "https://telegra.ph/file/fd3b8cc06dfd345d96362.jpg",
        "https://telegra.ph/file/6d909b4a1b7b0385c1dfe.jpg",
        "https://telegra.ph/file/17770ad693a43ebeb0fb6.jpg",
        "https://telegra.ph/file/fd3b8cc06dfd345d96362.jpg",
    ]
)



@bot.on(events.InlineQuery)
async def inline_handler(event):
    builder = event.builder
    result = None
    query = event.text
    user = await Uputt.get_me()
    uid = user.id
    if event.query.user_id == user.id and query.startswith(
            "@UputtSupport"):
        buttons = paginate_help(0, CMD_HELP, "helpme")
        result = await event.builder.photo(
            file=logouputt,
            link_preview=False,
            text=f"**✨ ᴜᴘᴜᴛᴛ-ᴜsᴇʀʙᴏᴛ ɪɴʟɪɴᴇ ᴍᴇɴᴜ ✨**\n\n⍟ **ᴅᴇᴘʟᴏʏ :** •[{HOSTED_ON}]•\n⍟ **ᴏᴡɴᴇʀ :** {user.first_name}\n⍟ **ᴊᴜᴍʟᴀʜ :** {len(CMD_HELP)} **Modules**",
            buttons=main_help_button,
        )
    elif query.startswith("repo"):
        result = builder.article(
            title="Repository",
            description="Repository Uputt-Userbot",
            url="https://t.me/UputtSupport",
            thumb=InputWebDocument(
                var.INLINE_PIC,
                0,
                "image/jpeg",
                []),
            text="**Uputt-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n✧  **ʀᴇᴘᴏ :** [Uputt](https://t.me/iamuput)\n✧ **sᴜᴘᴘᴏʀᴛ :** @UputtSupport\n✧ **ʀᴇᴘᴏsɪᴛᴏʀʏ :** [Uputt-Userbot](https://github.com/iamuput/Uputt-Userbot)\n➖➖➖➖➖➖➖➖➖➖",
            buttons=[
                [
                    custom.Button.url(
                        "ɢʀᴏᴜᴘ",
                        "https://t.me/UputtSupport"),
                    custom.Button.url(
                        "ʀᴇᴘᴏ",
                        "https://github.com/iamuput/Uputt-Userbot"),
                ],
            ],
            link_preview=False,
        )
    elif query.startswith("Inline buttons"):
        markdown_note = query[14:]
        prev = 0
        note_data = ""
        buttons = []
        for match in BTN_URL_REGEX.finditer(markdown_note):
            n_escapes = 0
            to_check = match.start(1) - 1
            while to_check > 0 and markdown_note[to_check] == "\\":
                n_escapes += 1
                to_check -= 1
            if n_escapes % 2 == 0:
                buttons.append(
                    (match.group(2), match.group(3), bool(
                        match.group(4))))
                note_data += markdown_note[prev: match.start(1)]
                prev = match.end(1)
            elif n_escapes % 2 == 1:
                note_data += markdown_note[prev:to_check]
                prev = match.start(1) - 1
            else:
                break
        else:
            note_data += markdown_note[prev:]
        message_text = note_data.strip()
        tl_ib_buttons = ibuild_keyboard(buttons)
        result = builder.article(
            title="Inline creator",
            text=message_text,
            buttons=tl_ib_buttons,
            link_preview=False,
        )
    else:
        result = builder.article(
            title="✨ ᴜᴘᴜᴛᴛ-ᴜsᴇʀʙᴏᴛ ✨",
            description="Uputt-Userbot | Telethon",
            url="https://t.me/UputtSupport",
            thumb=InputWebDocument(
                var.INLINE_PIC,
                0,
                "image/jpeg",
                []),
            text=f"**Uputt-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n✧ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n✧ **ᴀssɪsᴛᴀɴᴛ:** {var.BOT_USERNAME}\n➖➖➖➖➖➖➖➖➖➖\n**ᴜᴘᴅᴀᴛᴇs :** @skandallgua\n➖➖➖➖➖➖➖➖➖➖",
            buttons=[
                [
                    custom.Button.url(
                        "ɢʀᴏᴜᴘ",
                        "https://t.me/UputtSupport"),
                    custom.Button.url(
                        "ʀᴇᴘᴏ",
                        "https://github.com/iamuput/Uputt-Userbot"),
                ],
            ],
            link_preview=False,
        )
    await event.answer(
        [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
    )
