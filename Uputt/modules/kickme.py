# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.channels import LeaveChannelRequest

from Uputt import CMD_HELP
from Uputt.iamuput import uputt_cmd, eor

from . import cmd, var


@uputt_cmd(pattern="kickme$", allow_sudo=False)
async def kickme(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await eor(
            event,
            "**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok..."
        )
    user = await event.client.get_me()
    await eor(event, f"`{user.first_name} telah meninggalkan grup ini, selamat tinggal!!`")
    await event.client.kick_participant(event.chat_id, "me")


@uputt_cmd(pattern="kikme$", allow_sudo=False)
async def kikme(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await eor(
            event, "**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok..."
        )
    await eor(event, "**GC NYA JELEK GOBLOK KELUAR DULU AH CROTT** 🥴")
    await event.client.kick_participant(event.chat_id, "me")


@uputt_cmd(pattern="leaveall$", allow_sudo=False)
async def kickmeall(event):
    Putt = await eor(event, "`[Proses] - Keluar Dari Semua Obrolan Grup...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await event.client(LeaveChannelRequest(chat))
            except BaseException:
                er += 1
    await Putt.edit(f"**Berhasil Keluar dari {done} Group, Gagal Keluar dari {er} Group**"
    )


CMD_HELP.update(
    {
        "Kickme": f"**Plugin : **`Kickme`\
        \n\n  »  **Perintah :** `{cmd}kickme`\
        \n  »  **Kegunaan : **Keluar grup dengan menampilkan pesan Master has left this group, bye!!\
        \n\n  »  **Perintah :** `{cmd}kikme`\
        \n  »  **Kegunaan : **Keluar grup dengan menampilkan pesan GC NYA JELEK GOBLOK KELUAR DULU AH CROTT 🥴\
        \n\n  »  **Perintah :** `{cmd}leaveall`\
        \n  »  **Kegunaan : **Keluar dari semua grup telegram yang anda gabung.\
    "
    }
)
