# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from time import sleep
from Uputt import CMD_HELP
from Uputt.iamuput import uputt_cmd

from . import cmd


@uputt_cmd(pattern="cacad(?: |$)(.*)")
async def _(x):
    uputt = await x.reply("**Cacad 😏**")
    sleep(2)
    await uputt.edit("**Najis Akunnya Cacad 😂**")
    sleep(1)
    await uputt.edit("*Hahahaha Cacad 🤣**")
    sleep(2)
    await uputt.edit("**Canda Akun Cacad 😂🤣**")


@uputt_cmd(pattern="hayo(?: |$)(.*)")
async def _(d):
    uputt = await d.reply("**Hayolo 😂**")
    sleep(1)
    await uputt.edit("**Hayoloo 😭**")
    sleep(1)
    await uputt.edit("**Hayolooo 😆**")
    sleep(1)
    await uputt.edit("**Hayoloooo 😭🕺**")
    sleep(3)
    await uputt.edit("**Hayolooooo 👻**")
    sleep(2)
    await uputt.edit("**Haayolooooo 🤭**")
    sleep(2)
    await uputt.edit("**Botnya Mati Ya?**")
    sleep(2)
    await uputt.edit("**Botnya Mati Ya? kasiaaaan** 😭🤌")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "PuttUbot6": f"**Plugin : **`PuttUbot6`\
        \n\n  »  **Perintah :** `{cmd}cacad`\
        \n  »  **Kegunaan :** Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}hayolo`\
        \n  »  **Kegunaan :** Coba Senditi Tod.\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
