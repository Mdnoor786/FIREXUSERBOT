#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

# $$$$$$$$$$$$$$$$$¢$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$¢$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$¢

GENDER = [
    "u is mard",
    "u is man",
    "u is eviralt",
    "u is woman",
    "u is gey",
    "u is chakka",
]

EMOTICONS = [
    "(҂⌣̀_⌣́)",
    "（；¬＿¬)",
    "(-｡-;",
    "┌[ O ʖ̯ O ]┐",
    "〳 ͡° Ĺ̯ ͡° 〵",
]

WAVING = [
    "(ノ^∇^)",
    "(;-_-)/",
    "@(o・ェ・)@ノ",
    "ヾ(＾-＾)ノ",
    "ヾ(◍’౪◍)ﾉﾞ♡",
    "(ό‿ὸ)ﾉ",
    "(ヾ(´・ω・｀)",
]

WTF = [
    "༎ຶ‿༎ຶ",
    "(‿ˠ‿)",
    "╰U╯☜(◉ɷ◉ )",
    "(;´༎ຶ益༎ຶ)♡",
    "╭∩╮(︶ε︶*)chu",
    "( ＾◡＾)っ (‿|‿)",
]

LOB = [
    "乂❤‿❤乂",
    "(｡♥‿♥｡)",
    "( ͡~ ͜ʖ ͡°)",
    "໒( ♥ ◡ ♥ )७",
    "༼♥ل͜♥༽",
]

CONFUSED = [
    "(・_・ヾ",
    "｢(ﾟﾍﾟ)",
    "﴾͡๏̯͡๏﴿",
    "(￣■￣;)!?",
    "▐ ˵ ͠° (oo) °͠ ˵ ▐",
    "(-_-)ゞ゛",
]

DEAD = [
    "(✖╭╮✖)",
    "✖‿✖",
    "(+_+)",
    "(✖﹏✖)",
    "∑(✘Д✘๑)",
]

SED = [
    "(＠´＿｀＠)",
    "⊙︿⊙",
    "(▰˘︹˘▰)",
    "●︿●",
    "(　´_ﾉ` )",
    "彡(-_-;)彡",
]

DOG = [
    "-ᄒᴥᄒ-",
    "◖⚆ᴥ⚆◗",
]

SHRUG = [
    "( ͡° ͜ʖ ͡°)",
    "¯\_(ツ)_/¯",
    "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
    "ʕ•ᴥ•ʔ",
    "(▀ Ĺ̯▀   )",
    "(ง ͠° ͟ل͜ ͡°)ง",
    "༼ つ ◕_◕ ༽つ",
    "ಠ_ಠ",
    "(☞ ͡° ͜ʖ ͡°)☞",
    "¯\_༼ ି ~ ି ༽_/¯",
    "c༼ ͡° ͜ʖ ͡° ༽⊃",
]

# ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓


@bot.on(admin_cmd(pattern="gendar$", outgoing=True))
@bot.on(sudo_cmd(pattern="gendar$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(GENDER)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="shrug$", outgoing=True))
@bot.on(sudo_cmd(pattern="shrug$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(SHRUG)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="dome", outgoing=True))
@bot.on(sudo_cmd(pattern="dome", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(DOG)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="mesed$", outgoing=True))
@bot.on(sudo_cmd(pattern="mesed$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(SED)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="medead$", outgoing=True))
@bot.on(sudo_cmd(pattern="medead$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(DEAD)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="confused$", outgoing=True))
@bot.on(sudo_cmd(pattern="confused$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(CONFUSED)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="lobb$", outgoing=True))
@bot.on(sudo_cmd(pattern="lobb$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(LOB)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="wut$", outgoing=True))
@bot.on(sudo_cmd(pattern="wut$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(WTF)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="wavee$", outgoing=True))
@bot.on(sudo_cmd(pattern="wavee$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(WAVING)
    await edit_or_reply(e, txt)


@bot.on(admin_cmd(pattern="hehe$", outgoing=True))
@bot.on(sudo_cmd(pattern="hehe$", allow_sudo=True))
async def metoo(e):
    if e.fwd_from:
        return
    txt = random.choice(EMOTICONS)
    await edit_or_reply(e, txt)


CmdHelp("edits").add_command("hehe", None, "Use and see").add_command(
    "wavee", None, "Use and see"
).add_command("wut", None, "Use and see").add_command(
    "lobb", None, "Use and see"
).add_command(
    "confused", None, "Use and see"
).add_command(
    "medead", None, "Use and see"
).add_command(
    "mesed", None, "Use and see"
).add_command(
    "dome", None, "Use and see"
).add_command(
    "shrug", None, "Use and see"
).add_command(
    "gendar", None, "Use and see"
).add()
