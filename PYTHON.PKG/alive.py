import time

from telethon import version
from userbot import ALIVE_NAME, StartTime, PYTHONversion
from PYTHONBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "✞︎t͛ẞ̸ PYTHONẞø✞︎ 🇮🇳"
PYTHON_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂-ℓx Choice PYTHONẞø✞︎"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@Python_Userbot_Support"

Legend = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={Legend-Lx})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  PYTHON_IMG:
        PYTHON_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        PYTHON_caption += f"______𝙿𝚈𝚃𝙷𝙾𝙽-𝐔𝐬𝐞𝐫𝐛𝐨𝐭______\n"
        PYTHON_caption += f"╔════❰🐍 Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ🐍 ❱═❍⊱❁۪۪¤๋͜\n"
        PYTHON_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        PYTHON_caption += f"║┣⪼ Ⲟⲱⲛⲉʀ     ┣⪼ [ℓєgєи∂-ℓx](t.me/Legendl_Mr_Hacker) \n"
        PYTHON_caption += f"║┣⪼ Ⲋⲧⲁⲧυⲋ      ┣⪼ Ⲟⲛⳑⲓⲛⲉ\n"
        PYTHON_caption += f"║┣⪼ Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ ┣⪼ {mention}\n"
        PYTHON_caption += f"║┣⪼ Ⳙⲣⲧⲓⲙⲉ      ┣⪼  {uptime}\n"
        PYTHON_caption += f"║┣⪼ Ⲃⲟⲧ Ⲣⲓⲛⳋ    ┣⪼  {}\n"   
        PYTHON_caption += f"║┣⪼ Ⲣⲩⲧⲏⲟⲛ      ┣⪼  {PYTHONversion}\n"
        PYTHON_caption += f"║┣⪼ Ⲧⲉⳑⲉⲧⲏⲟⲛ     ┣⪼  {version.__version__} \n"
        PYTHON_caption += f"║┣⪼ [✨🐍PYTHON┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/Python_Userbot_Support)\n"
        PYTHON_caption += f"║╰━━━━━━━━━━━━━━━➣ \n"
        PYTHON_caption += f"╚══════════════════❍⊱❁۪۪¤๋͜-  \n"
        
        await alive.client.send_file(
            alive.chat_id, PYTHON_IMG, caption=PYTHON_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         𝕭𝖔𝖙 𝕾𝖙𝖆𝖙𝖚𝖘\n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 ℓєgєи∂ϐοτ  : `{PYTHONversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/Legend_Mr_Hacker)\n"
        )

CmdHelp("𝚋𝚘𝚝𝚜𝚝𝚊𝚝𝚜").add_command(
    'bot', None, 'υѕє αи∂ ѕєє'
).add()

