# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.errors import FloodWaitError

from Uputt import CMD_HELP
from Uputt.events import register
from Uputt.iamuput import UputtChanger, uputt_cmd, eod, eor
from Uputt.database.bl_gcast import add_gcast, cek_gcast, del_gcast

from . import (
    DEVS,
    GCAST_BLACKLIST,
    cmd
)


@uputt_cmd(pattern="gcast(?: |$)(.*)")
async def gcast(event):
    me = await event.client.get_me()
    BLACKLIST_GCAST = UputtChanger(cek_gcast(me.id))
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        reply = await event.get_reply_message()
        msg = reply.text
    else:
        return await eod(event, "**Pesannya mana anjjj**")
    kk = await eor(event, "`Sabar kontttolll, lagi kirimm gikesann luu ni monyet`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    await event.client.send_message(chat, msg, file=reply.media if reply else None)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg, file=reply.media if reply else None)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Ngewe Ke** {done} **Grup Tod.**\n**Sorry Tod Gagal Ngewe Ke** {er} **Grup.**"
    )


@uputt_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        reply = await event.get_reply_message()
        msg = reply.text
    else:
        return await eod(event, "**Pesannya mana anjjj**")
    kk = await eor(event, "`Sabar kontttolll, lagi kirimm gikesann luu ni monyet...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg, file=reply.media if reply else None)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg, file=reply.media if reply else None)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Ngewe Ke** {done} **User Tod.**\n**Sorry Tod Gagal Ngewe Pesan Ke** {er} **User.**"
    )


@uputt_cmd(pattern="listbl$")
async def sudo(event):
    me = await event.client.get_me()
    BLACKLIST_GCAST = UputtChanger(cek_gcast(me.id))
    text = '\n'
    if BLACKLIST_GCAST:
        for bl in BLACKLIST_GCAST:
            text += f"   » {bl}\n"
        await eor(
            event, 
            f"""
**🔮 Blacklist GCAST:** `Enabled`

📚 **Blacklist Group:**
{text}

Ketik `{cmd}addbl` di grup yang ingin anda tambahkan ke daftar blacklist gcast."""
        )
    else:
        await eod(event, "**🔮 Blacklist GCAST:** `Disabled`")


@uputt_cmd(pattern="addbl(?:\\s|$)([\\s\\S]*)")
@register(incoming=True, from_users=DEVS, pattern=r"^Addbl$")
async def add(event):
    me = await event.client.get_me()
    BLACKLIST_GCAST = UputtChanger(cek_gcast(me.id))
    xxnx = await eor(event, '**Memproses...**')
    if event.chat_id in BLACKLIST_GCAST:
        await eod(
            event,
            "**Grup ini sudah ada dalam daftar blacklist gcast.**"
        )
        return
    else:
        add_gcast(me.id, event.chat_id)
        await xxnx.edit(
            f"**Berhasil Menambahkan** `{event.chat_id}` **ke daftar blacklist gcast.**"
        )


@uputt_cmd(pattern="delbl(?:\\s|$)([\\s\\S]*)")
@register(incoming=True, from_users=DEVS, pattern=r"^delbl$")
async def _(event):
    xxx = await eor(event, '**Memproses...**')
    me = await event.client.get_me()
    BLACKLIST_GCAST = UputtChanger(cek_gcast(me.id))
    gc = event.chat_id
    if gc in BLACKLIST_GCAST:
        del_gcast(me.id, gc)
        await xxx.edit(f"**Berhasil Menghapus** `{gc}` **dari daftar blacklist gcast.**"
        )
    else:
        await eod(
            xxx,
            "**Grup ini tidak ada dalam daftar blacklist gcast.**",
            time=45
        )


CMD_HELP.update(
    {
        "Gcast": f"**Plugin : **`Gcast`\
        \n\n  »  **Perintah :** `{cmd}gcast` <text/reply media>\
        \n  »  **Kegunaan : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
        \n\n  »  **Perintah :** `{cmd}listbl`\
        \n  »  **Kegunaan : **Untuk Mengecek informasi daftar blacklist gcast.\
        \n\n  »  **Perintah :** `{cmd}addbl`\
        \n  »  **Kegunaan : **Untuk Menambahkan grup tersebut ke blacklist gcast.\
        \n\n  »  **Perintah :** `{cmd}delbl`\
        \n  »  **Kegunaan : **Untuk Menghapus grup tersebut dari blacklist gcast.\
        \n  �?  **Note : **Ketik perintah** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **di grup yang kamu Blacklist.\
    "
    }
)


CMD_HELP.update(
    {
        "Gucast": f"**Plugin : **`Gucast`\
        \n\n  »  **Perintah :** `{cmd}gucast` <text/reply media>\
        \n  »  **Kegunaan : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
                    )
