import os
import asyncio
import config
from telethon import events, Button
from telethon.tl.custom import button
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9

ALIVE_IMG = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_IMG = ALIVE_IMG
else:
    DEADLY_IMG = "https://te.legra.ph/file/2e2f78610814092d61103.jpg"

OWNER_INFO = config.OWNER_NAME
if config.OWNER_NAME:
    OWNER_NAME = OWNER_INFO
else:
    OWNER_NAME =@Shinu_han

OWNER_ID = config.OWNER_ID

Deadly_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/+Tb6gszRw5a85MDE9"),
        Button.url("https://t.me/spam_botts")
        ],
        [
      
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{sinu_hann}](tg://user?id={6248129136})"
        creator = f"[ ࿈ 𝙎𝙄𝙉𝙐 𝙃𝘼𝙉 ࿈ id=6248129136
        DEADLY_ON = f"""
ʜᴇʏ {mention},
ᴛʜɪs ɪs SINU SPAMM sᴘᴀᴍʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- {creator}!


ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- {shinu hann}

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- {shinu approx spamm}

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, DEADLY_IMG, caption=DEADLY_ON, buttons=Deadly_Button)
