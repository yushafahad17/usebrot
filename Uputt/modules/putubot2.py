# Copyright (C) 2021 Kyy - Userbot
# Credit by kyy
# Recode by @AyiinXd


from time import sleep

from Uputt import CMD_HELP
from Uputt.iamuput import uputt_cmd

from . import cmd

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@uputt_cmd(pattern=r"lipkol(?: |$)(.*)")
async def _(a):
    uputt = await a.reply("**Ayaaang** 🥺")
    sleep(2)
    await uputt.edit("**Kangeeen** 👉👈")
    sleep(1)
    await uputt.edit("**Pingiinn Slipkool Yaaang** 🥺👉👈")


# Create by myself @localheart


@uputt_cmd(pattern=r"nakal(?: |$)(.*)")
async def _(y):
    uputt = await y.reply("**Ayaaang Ih** 🥺")
    sleep(1)
    await uputt.edit("**Nakal Banget Dah Ayang** 🥺")
    sleep(1)
    await uputt.edit("**Aku Gak Like Ayang** 😠")
    sleep(1)
    await uputt.edit("**Pokoknya Aku Gak Like Ih** 😠")
  


@uputt_cmd(pattern=r"favboy(?: |$)(.*)")
async def _(i):
    uputt = await i.reply("**Duuhh Ada Cowo Ganteng** 👉👈")
    sleep(1.5)
    await uputt.edit("**You Are My Favorit Boy** 😍")
    sleep(1.5)
    await uputt.edit("**Kamu Harus Jadi Cowo Aku Ya** 😖")
    sleep(1.5)
    await uputt.edit("**Pokoknya Harus Jadi Cowo Aku** 👉👈")
    sleep(1.5)
    await uputt.edit("**Gak Boleh Ada Yang Lain** 😠")


@uputt_cmd(pattern=r"favgirl(?: |$)(.*)")
async def _(i):
    uputt = await i.reply("**Duuhh Ada Cewe Cantik** 👉👈")
    sleep(2)
    await uputt.edit("**You Are My Favorit Girl** 😍")
    sleep(2)
    await uputt.edit("**Kamu Harus Jadi Cewe Aku Ya** 😖")
    sleep(2)
    await uputt.edit("**Pokoknya Harus Jadi Cewe Aku** 👉👈")
    sleep(2)
    await uputt.edit("**Gak Boleh Ada Yang Lain** 😠")


@uputt_cmd(pattern=r"canlay(?: |$)(.*)")
async def _(n):
    uputt = await n.reply("**Eh Kamu Cantik-cantik**")
    sleep(2)
    await uputt.edit("**Kok Alay Banget**")
    sleep(2)
    await uputt.edit("**Spam Bot Mulu**")
    sleep(2)
    await uputt.edit("**Baru Bikin Userbot Ya??**")
    sleep(2)
    await uputt.edit("**Pantes Norak Xixixi**")


@uputt_cmd(pattern=r"ganlay(?: |$)(.*)")
async def _(x):
    uputt = await x.reply("**Eh Kamu Ganteng-ganteng**")
    sleep(2)
    await uputt.edit("**Kok Alay Banget**")
    sleep(2)
    await uputt.edit("**Spam Bot Mulu**")
    sleep(2)
    await uputt.edit("**Baru Bikin Userbot Ya??**")
    sleep(2)
    await uputt.edit("**Pantes Norak Xixixi**")


@uputt_cmd(pattern=r"ange(?: |$)(.*)")
async def _(d):
    uputt = await d.reply("**Ayanggg 😖**")
    sleep(1)
    await uputt.edit("**Aku Ange 😫**")
    sleep(1)
    await uputt.edit("**Ayuukk Picies Yang 🤤**")


CMD_HELP.update(
    {
        "PuttUbot2": f"**Plugin : **`PuttUbot2`\
        \n\n  »  **Perintah :** `{cmd}lipkol`\
        \n  »  **Kegunaan : **Ngajakin ayang slipkol\
        \n\n  »  **Perintah :** `{cmd}nakal`\
        \n  »  **Kegunaan : **Ga like ayang nakal\
        \n\n  »  **Perintah :** `{cmd}favboy`\
        \n  »  **Kegunaan : **Cowo idaman\
        \n\n  »  **Perintah :** `{cmd}favgirl`\
        \n  »  **Kegunaan : **Cewe idaman\
        \n\n  »  **Perintah :** `{cmd}canlay`\
        \n  »  **Kegunaan : **Ngatain si cantik alay\
        \n\n  »  **Perintah :** `{cmd}ganlay`\
        \n  »  **Kegunaan : **Ngatain si ganteng alay\
        \n\n  »  **Perintah :** `{cmd}ange`\
        \n  »  **Kegunaan : **Minta jatah ke ayang\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
  )
