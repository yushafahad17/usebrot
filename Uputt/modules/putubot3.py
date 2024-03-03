# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

from time import sleep

from Uputt import CMD_HELP
from Uputt.iamuput import uputt_cmd

from . import cmd

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@uputt_cmd(pattern=r"uput(?: |$)(.*)")
async def _(y):
    uputt = await y.reply("**Hai... Perkenalkan Nama Saya Putraa**")
    sleep(3)
    await uputt.edit("**Umur 21 Tahun...**")
    sleep(2)
    await uputt.edit("**Asli Batam, Tapi lagi di Pekanbaru...**")
    sleep(3)
    await uputt.edit("**Owner Dari [Uputt-Userbot](https://github.com/iamuput/Uputt-Userbot)... Salam Kenal** 😁")
# Create by myself @AyiinXd


@uputt_cmd(pattern=r"sayang(?: |$)(.*)")
async def _(i):
    xx = await i.reply("**Aku Cuma Mau Bilang...**")
    sleep(3)
    await xx.edit("**Aku Sayang Kamu Mwaahh** 😘❤")
# Create by myself @AyiinXd


@uputt_cmd(pattern=r"semangat(?: |$)(.*)")
async def _(n):
    uputt = await n.reply("**Apapun Yang Terjadi...**")
    sleep(3)
    await uputt.edit("**Tetaplah Bernafas...**")
    sleep(1)
    await uputt.edit("**Dan Bersyukur...**")
# Create by myself @AyiinXd


@uputt_cmd(pattern=r"mengeluh(?: |$)(.*)")
async def _(s):
    uputt = await s.reply("**Apapun Yang Terjadi...**")
    sleep(3)
    await uputt.edit("**Tetaplah Mengeluh...**")
    sleep(1)
    await uputt.edit("**Dan Putus Asa...**")
# Create by myself @AyiinXd


CMD_HELP.update(
    {
        "PuttUbot3": f"**Plugin : **`PuttUbot3`\
        \n\n  »  **Perintah :** `{cmd}uputt`\
        \n  »  **Kegunaan : **Perkenalan diri Uputt\
        \n\n  »  **Perintah :** `{cmd}sayang`\
        \n  »  **Kegunaan : **Bucin\
        \n\n  »  **Perintah :** `{cmd}semangat`\
        \n  »  **Kegunaan : **Memberikan semangat!\
        \n\n  »  **Perintah :** `{cmd}mengeluh`\
        \n  »  **Kegunaan : **Ngeledek\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
