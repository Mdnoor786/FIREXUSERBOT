from . import *


@bot.on(admin_cmd(pattern="gdaftrnoon(.*)"))
async def xd(event):
    await event.edit("Sending To all Group good AfterNoon")
    event.pattern_match.group(1)
    async for tele in borg.iter_dialogs():
        if tele.is_group:
            chat = tele.id
            lol = 0
            done = 0
            try:
                await bot.send_message(
                    chat,
                    "╭━━━┳━━━┳━━━┳━━━╮\\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\\n╰━━━┻━━━┻━━━┻━━━╯\\n╭━━━╮\\n┃╭━╮┃\\n┃┃╱┃┃\\n┃╰━╯┃\\n┃╭━╮┃\\n╰╯╱╰╯\\n╭━━━╮\\n┃╭━━╯\\n┃╰━━╮\\n┃╭━━╯\\n┃┃\\n╰╯\\n╭━━━━╮\\n┃╭╮╭╮┃\\n╰╯┃┃╰╯\\n╱╱┃┃\\n╱╱┃┃\\n╱╱╰╯\\n╭━━━╮\\n┃╭━━╯\\n┃╰━━╮\\n┃╭━━╯\\n┃╰━━╮\\n╰━━━╯\\n╭━━━╮\\n┃╭━╮┃\\n┃╰━╯┃\\n┃╭╮╭╯\\n┃┃┃╰╮\\n╰╯╰━╯\\n╭━╮╱╭╮\\n┃┃╰╮┃┃\\n┃╭╮╰╯┃\\n┃┃╰╮┃┃\\n┃┃╱┃┃┃\\n╰╯╱╰━╯\\n╭━━━╮\\n┃╭━╮┃\\n┃┃╱┃┃\\n┃┃╱┃┃\\n┃╰━╯┃\\n╰━━━╯\\n╭━━━╮\\n┃╭━╮┃\\n┃┃╱┃┃\\n┃┃╱┃┃\\n┃╰━╯┃\\n╰━━━╯\\n╭━╮╱╭╮\\n┃┃╰╮┃┃\\n┃╭╮╰╯┃\\n┃┃╰╮┃┃\\n┃┃╱┃┃┃\\n╰╯╱╰━╯",
                )

                done += 1
            except:
                lol += 1
    await event.reply("#Smoothest & Fastest [FIRE-X](https://t.me/FirexSupport)")


CmdHelp("gdaftrnoon").add_command(
    "gdaftrnoon", None, "Wishs Good Afternoon in all groups just one command"
).add()
