from time import sleep

from Uputt import CMD_HELP
from Uputt.iamuput import uputt_cmd

from . import cmd

@uputt_cmd(pattern=r"ngentot(?: |$)(.*)")
async def _(uputt):
    putt = await uputt.reply("**WOYY NGENTOD!!**")
    sleep(1)
    await putt.edit("**JANGAN SOK JAGOAN DAH LU**")
    sleep(3)
    await putt.edit("**MUKA MASIH KAYA KONTOL AJA**")
    sleep(3)
    await putt.edit("**BANGGA LU HAHAHAHA**")
    sleep(3)
    await putt.edit("**COBA DEH NGACA MUKA LU KAN HINA BANGET**")
    sleep(3)
    await putt.edit("**HAHAHAHA**")
    sleep(3)
    await putt.edit("**MAKANYA GANTENG KONTOL**")
    sleep(3)
    await putt.edit("**BIAR MUKALU GAK DIHINA TERUS**")
    sleep(3)
    await putt.edit("**SAMA ORANG LAIN**")
    sleep(3)
    await putt.edit("**HAHAHAHA**")
# Create by myself @localheart


@uputt_cmd(pattern=r"goblok(?: |$)(.*)")
async def _(gblk):
    uputt = await gblk.reply("**WOYY GOBLOK!!**")
    sleep(3)
    await uputt.edit("**KO LU GOBLOK BANGET SIH**")
    sleep(3)
    await uputt.edit("**OTAK LU TUH KAYA KONTOL**")
    sleep(3)
    await uputt.edit("**YANG LEMBEK KETIKA LEMAH**")
    sleep(3)
    await uputt.edit("**DAN KERAS KETIKA LU SANGE GOBLOK**")
    sleep(3)
    await uputt.edit("**HAHAHAHA**")
    sleep(3)
    await uputt.edit("**MAKANYA JANGAN SANGEAN MULU**")
    sleep(3)
    await uputt.edit("**MUKA LU AJA KAYA ASPAL JALANAN**")
    sleep(3)
    await uputt.edit("**EHHH SANGE NYA MAU DAPAT YANG CANTIK**")
    sleep(3)
    await uputt.edit("**HAHAHAHA**")
# Create by myself @localheart


@uputt_cmd(pattern=r"ngatain(?: |$)(.*)")
async def _(kntl):
    kon = await kntl.reply("**BABI!!**")
    sleep(3)
    await kon.edit("**MUKA LU KAYA BABI**")
    sleep(3)
    await kon.edit("**OTAK LU TUH KAYA KONTOL**")
    sleep(3)
    await kon.edit("**MUKA LU HINA BANGET**")
    sleep(3)
    await kon.edit("**OTAK LU KAYA BATU**")
    sleep(3)
    await kon.edit("**HAHAHAHA**")
    sleep(3)
    await kon.edit("**MAKANYA JANGAN SANGEAN MULU**")
    sleep(3)
    await kon.edit("**KONTOL LU AJA MASIH BENGKOK**")
    sleep(3)
    await kon.edit("**EHHH SANGE NYA MAU DAPAT YANG CANTIK**")
    sleep(3)
    await kon.edit("**HAHAHAHA**")
# Create by myself @localheart


@uputt_cmd(pattern=r"yatim(?: |$)(.*)")
async def _(ytim):
    iamuput = await ytim.reply("`Hai Anak Kontol 🙈, Jangan Lupa Makan Yaa`")
    sleep(3)
    await iamuput.edit("`Jangan Bilang Lu Ga Dikasih Makan Sama Ortu 😁`")
    sleep(3)
    await iamuput.edit("`APA PERLU GUA SANTUNIN ?? 🙈🙈 xixixi`")
    sleep(3)
    await iamuput.edit("`OH IYAA LUPAAA, LU KAN BEBAN KELUARGA 🤣`")
    sleep(3)
    await iamuput.edit("`MANA MUNGKIN ORTU LU PEDULII xixixi 🙈`")
    sleep(3)
    await iamuput.edit("`KETAWA DULU BOLEH KALI YAA 😁`")
    sleep(3)
    await iamuput.edit("`HAHAHAHAHAHAHA`")
    sleep(3)
    await iamuput.edit("`KASIAN ORTUNYAA GAPEDULIII 🙈🤣`")
    sleep(3)
    await iamuput.edit("`MAAF YA, CANDAA BEBANNNN xixixi 🙈`")
    sleep(3)
    await iamuput.edit("`Tapi Bo'ong Hiyahiyahiya`")
# Create by myself @localheart


@uputt_cmd(pattern=r"kont(?: |$)(.*)")
async def _(kontol):
    putt = await kontol.reply("**WOYY NGENTOD!!**")
    sleep(3)
    await putt.edit("**LU ANAK KONTOLL**")
    sleep(3)
    await putt.edit("**DI BIKIN DARI KONTOLL**")
    sleep(3)
    await putt.edit("**MUKALU PERSIS KONTOLL**")
    sleep(3)
    await putt.edit("**DASAR ANAK NGONTOLLLL**")
    sleep(3)
    await putt.edit("**NOLEP KONTOLL**")
    sleep(3)
    await putt.edit("**NGERUSUH KONTOLL**")
    sleep(3)
    await putt.edit("**BENER BENER KONTOLL**")
    sleep(3)
    await putt.edit("**PADAHAL LO GAPUNYA KONTOLL**")
    sleep(3)
    await putt.edit("**MENDING LO OPERASI KONTOLL**")
    sleep(3)
    await putt.edit("**BIAR LO PUNYA KONTOLL**")
    sleep(3)
    await putt.edit("**KASIAN CACAD GAPUNYA KONTOLL**")

CMD_HELP.update(
    {
        "PuttToxic2": f"**Plugin : **`PuttToxic2`\
        \n\n  »  **Perintah :** `{cmd}ngentot`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}goblok`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}ngatain`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}kont`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}yatim`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
                  )
