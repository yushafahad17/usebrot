""" Userbot module for other small commands. """

from Uputt import CMD_HELP
from Uputt.iamuput import uputt_cmd, eor
from Uputt.database.variable import cek_var

from . import cmd


@uputt_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await eor(
        event,
        f"""
**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `{cmd}help` Atau Bisa Minta Bantuan Ke:
⍟ **Group Support :** [𝚂𝚄𝙿𝙿𝙾𝚁𝚃](t.me/UputtSupport)
⍟ **Channel :** [𝙲𝙷𝙰𝙽𝙽𝙴𝙻](t.me/Flukosaa)
⍟ **Owner Bot :** [𝚄𝙿𝚄𝚃](t.me/iamuput)
⍟ **Repo :** [𝚄𝙿𝚄𝚃𝚃-𝚄𝚂𝙴𝚁𝙱𝙾𝚃](https://github.com/iamuput/Uputt-Userbot)
"""
    )


@uputt_cmd(pattern="listvar$")
async def var(event):
    text = "**Hasil database vars ditemukan.**\n\n**No | Variable | Value**"
    no = 0
    listvar = cek_var()
    if listvar:
        for xd in listvar:
            no += 1
            text += f"\n{no}. {xd[0]} - {xd[1]}"
    else:
        text = "**Anda Belum memiliki database vars.**"
    await eor(
        event,
        text
    )


CMD_HELP.update(
    {
        "Helper": f"**Plugin : **`Helper`\
        \n\n  »  **Perintah :** `{cmd}ihelp`\
        \n  »  **Kegunaan : **Bantuan Untuk Uputt-Userbot.\
        \n\n  »  **Perintah :** `{cmd}listvar`\
        \n  »  **Kegunaan : **Melihat Daftar Vars.\
        \n\n  »  **Perintah :** `{cmd}repo`\
        \n  »  **Kegunaan : **Melihat Repository Uputt-Userbot.\
        \n\n  »  **Perintah :** `{cmd}string`\
        \n  »  **Kegunaan : **Link untuk mengambil String Session.\
    "
    }
)
