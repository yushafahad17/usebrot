# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for filter commands """

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from Uputt import CMD_HELP
from Uputt.iamuput import uputt_cmd, eor

from . import cmd


@uputt_cmd(pattern="hentai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@nHentaiBot"
    xx = await eor(event, "**Memproses...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=424466890)
            )
            await event.client.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await event.client.send_message(chat, link)
            response = await response
        if response.text.startswith("Sorry I couldn't get manga from"):
            await xx.edit("**Maaf terjadi kesalahan...**")
        else:
            await xx.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "Hentai": f"**Plugin : **`Hentai`\
        \n\n  »  **Perintah :** `{cmd}hentai` <link nhentai>\
        \n  »  **Kegunaan : **Melihat nhentai di telegra.ph XD\
    "
    }
)
