from . import *


@bot.on(admin_cmd(pattern="gdevng(.*)"))
async def xd(event):
    await event.edit("Sending To all Group good Evening")
    event.pattern_match.group(1)
    async for tele in borg.iter_dialogs():
        if tele.is_group:
            chat = tele.id
            lol = 0
            done = 0
            try:
                await bot.send_message(
                    chat,
                    "╭━━━╮\\n┃╭━╮┃\\n┃┃╱╰╯\\n┃┃╭━╮\\n┃╰┻━┃\\n╰━━━╯\\n╭━━━╮\\n┃╭━╮┃\\n┃┃╱┃┃\\n┃┃╱┃┃\\n┃╰━╯┃\\n╰━━━╯\\n╭━━━╮\\n┃╭━╮┃\\n┃┃╱┃┃\\n┃┃╱┃┃\\n┃╰━╯┃\\n╰━━━╯\\n╭━━━╮\\n╰╮╭╮┃\\n╱┃┃┃┃\\n╱┃┃┃┃\\n╭╯╰╯┃\\n╰━━━╯\\n╭━━━╮\\n┃╭━━╯\\n┃╰━━╮\\n┃╭━━╯\\n┃╰━━╮\\n╰━━━╯\\n╭╮╱╱╭╮\\n┃╰╮╭╯┃\\n╰╮┃┃╭╯\\n╱┃╰╯┃\\n╱╰╮╭╯\\n╱╱╰╯\\n╭━━━╮\\n┃╭━━╯\\n┃╰━━╮\\n┃╭━━╯\\n┃╰━━╮\\n╰━━━╯\\n╭━╮╱╭╮\\n┃┃╰╮┃┃\\n┃╭╮╰╯┃\\n┃┃╰╮┃┃\\n┃┃╱┃┃┃\\n╰╯╱╰━╯\\n╭━━╮\\n╰┫┣╯\\n╱┃┃\\n╱┃┃\\n╭┫┣╮\\n╰━━╯\\n╭━╮╱╭╮\\n┃┃╰╮┃┃\\n┃╭╮╰╯┃\\n┃┃╰╮┃┃\\n┃┃╱┃┃┃\\n╰╯╱╰━╯\\n╭━━━╮\\n┃╭━╮┃\\n┃┃╱╰╯\\n┃┃╭━╮\\n┃╰┻━┃\\n╰━━━╯\\n",
                )

                done += 1
            except:
                lol += 1
    await event.reply(
        "Good evening! I hope you had a good and productive day. Cheer up![FIRE-X](https://t.me/FirexSupport"
    )


CmdHelp("gdevng").add_command(
    "gdevng", None, "Wishs Good Evening in all groups just one command"
).add()
