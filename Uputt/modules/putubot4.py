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

@uputt_cmd(pattern=r"ywc(?: |$)(.*)")
async def _(a):
    await a.edit("**Oke Sama-sama**")


@uputt_cmd(pattern=r"jamet(?: |$)(.*)")
async def _(y):
    uputt = await y.edit("**WOIII**")
    sleep(1.5)
    await uputt.edit("**JAMETTT**")
    sleep(1.5)
    await uputt.edit("**CUMA MAU BILANG**")
    sleep(1.5)
    await uputt.edit("**GAUSAH SO ASIK**")
    sleep(1.5)
    await uputt.edit("**EMANG KENAL?**")
    sleep(1.5)
    await uputt.edit("**GAUSAH REPLY**")
    sleep(1.5)
    await uputt.edit("**KITA BUKAN KAWAN**")
    sleep(1.5)
    await uputt.edit("**GASUKA PC ANJING**")
    sleep(1.5)
    await uputt.edit("**BOCAH KAMPUNG**")
    sleep(1.5)
    await uputt.edit("**MENTAL TEMPE**")
    sleep(1.5)
    await uputt.edit("**LEMBEK NGENTOT🔥**")


@uputt_cmd(pattern=r"pp(?: |$)(.*)")
async def _(i):
    await i.reply("**PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆**")


@uputt_cmd(pattern=r"dp(?: |$)(.*)")
async def _(i):
    await i.reply("**MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!**")


@uputt_cmd(pattern=r"so(?: |$)(.*)")
async def _(n):
    await n.reply("**GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!**")


@uputt_cmd(pattern=r"met(?: |$)(.*)")
async def _(d):
    await d.reply("**NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA**")
  

@uputt_cmd(pattern=r"war(?: |$)(.*)")
async def _(a):
    await a.reply("**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN...**")


@uputt_cmd(pattern=r"wartai(?: |$)(.*)")
async def _(y):
    await y.reply("**WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK**")


@uputt_cmd(pattern=r"kismin(?: |$)(.*)")
async def _(i):
    await i.reply("**CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!**")
  

@uputt_cmd(pattern=r"ded(?: |$)(.*)")
async def _(i):
    await i.reply("**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**")


@uputt_cmd(pattern=r"sokab(?: |$)(.*)")
async def _(n):
    await n.reply("**SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!**")


@uputt_cmd(pattern=r"gembel(?: |$)(.*)")
async def _(x):
    await x.reply("**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!**")


@uputt_cmd(pattern=r"cuih(?: |$)(.*)")
async def _(d):
    await d.reply("**GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!**")


@uputt_cmd(pattern=r"dih(?: |$)(.*)")
async def _(y):
    await y.reply("**DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!**")


@uputt_cmd(pattern=r"skb(?: |$)(.*)")
async def _(n):
    await n.reply("**EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK**")


@uputt_cmd(pattern=r"virtual(?: |$)(.*)")
async def _(s):
    uputt = await s.reply("**OOOO... INI YANG VIRTUAL**")
    sleep(1.5)
    await uputt.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await uputt.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await uputt.edit("**NI INGET**")
    sleep(1.5)
    await uputt.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await uputt.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await uputt.edit("**BHAHAHAHA**")
    sleep(1.5)
    await uputt.edit("**KASIAN MANA MASIH MUDA**")


CMD_HELP.update(
    {
        "PuttUbot4": f"**Plugin : **`PuttUbot4`\
        \n\n  »  **Perintah :** `{cmd}jamet`\
        \n  »  **Kegunaan : **Menghina Jamet telegram\
        \n\n  »  **Perintah :** `{cmd}pp`\
        \n  »  **Kegunaan : **Menghina Jamet telegram yang ga pake foto profil\
        \n\n  »  **Perintah :** `{cmd}dp`\
        \n  »  **Kegunaan : **Menghina Jamet muka hina!\
        \n\n  »  **Perintah :** `{cmd}so`\
        \n  »  **Kegunaan : **Ngeledek orang sokab\
        \n\n  »  **Perintah :** `{cmd}nb`\
        \n  »  **Kegunaan : **Ngeledek orang norak baru pake bot\
        \n\n  »  **Perintah :** `{cmd}skb`\
        \n  »  **Kegunaan : **Ngeledek orang sokab versi 2\
        \n\n  »  **Perintah :** `{cmd}met`\
        \n  »  **Kegunaan : **Ngeledek si jamet caper\
        \n\n  »  **Perintah :** `{cmd}war`\
        \n  »  **Kegunaan : **Ngeledek orang so keras ngajak war\
        \n\n  »  **Perintah :** `{cmd}wartai`\
        \n  »  **Kegunaan : **Ngeledek orang so ketrigger ngajak cod minta sharelok\
        \n\n  »  **Perintah :** `{cmd}kismin`\
        \n  »  **Kegunaan : **Ngeledek orang kismin so jagoan di tele\
        \n\n  »  **Perintah :** `{cmd}ded`\
        \n  »  **Kegunaan : **Nyuruh orang mati aja goblok wkwk\
        \n\n  »  **Perintah :** `{cmd}sokab`\
        \n  »  **Kegunaan : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  »  **Perintah :** `{cmd}gembel`\
        \n  »  **Kegunaan : **Ngeledek bapaknya si jamet\
        \n\n  »  **Perintah :** `{cmd}cuih`\
        \n  »  **Kegunaan : **Ngeludahin keluarganya satu satu wkwk\
        \n\n  »  **Perintah :** `{cmd}dih`\
        \n  »  **Kegunaan : **Ngeledek anak haram\
        \n\n  »  **Perintah :** `{cmd}gcs`\
        \n  »  **Kegunaan : **Ngeledek gc sampah\
        \n\n  »  **Perintah :** `{cmd}virtual`\
        \n  »  **Kegunaan : **Ngeledek orang pacaran virtual\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
