# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import os
import sys

from Uputt import CMD_HELP
from Uputt.iamuput import uputt_cmd, runcmd

from . import cmd


@uputt_cmd(pattern="getdb")
async def db_backup(e):
    if os.path.exists('uputt.db'):
        await e.client.send_file(
            entity=e.chat_id,
            file='iamuput.db',
            thumb="Uputt/resources/logo.jpg",
            caption=f'Database {(await e.client.get_me()).first_name}',
            force_document=True,
        )
        return
    else:
        await e.edit("Maaf database tidak ditemukan.")
        return


@uputt_cmd(pattern="setdb")
async def db_backup(e):
    xx = await e.reply("**Memproses...**")
    path = os.getcwd()
    reply = await e.get_reply_message()
    if 'iamuput.db' in os.listdir():
        await xx.edit("**Database `iamuput.db` ditemukan. Menghapus `iamuput.db` Dari Directory.**")
        os.remove('iamuput.db')
    media = reply.media
    if hasattr(media, "document"):
        file_doc = await reply.download_media()
        os.path.join(path, file_doc)
        await runcmd(f"cp {path}/{file_doc} {path}/iamuput.db")
        await xx.delete()
        await e.reply("**Database Berhasil digunakan. Sedang merestart userbot**")
        args = [sys.executable, "-m", "Uputt"]
        os.execle(sys.executable, *args, os.environ)


CMD_HELP.update(
    {
        "Database": f"**Plugin : **`Database`\
        \n\n  »  **Perintah :** `{cmd}getdb`\
        \n  »  **Kegunaan : **Untuk mengambil database anda.\
        \n\n  »  **Perintah :** `{cmd}setdb [reply document]`\
        \n  »  **Kegunaan : ** Balas ke Pesan Document untuk mengatur database anda yang sebelumnya telah anda ambil.\
        \n\n **CATATAN :** Simpan database anda dengan baik agar anda dapat menggunakannya kembali dengan perintah `{cmd}setdb`\
    "
    }
)
