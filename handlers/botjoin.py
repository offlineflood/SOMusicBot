from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["Qoşul", "asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Məni əvvəlcə admim etməlisiniz</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Sesmusic Asistan"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Senin İsteğin Üzerine Geldim")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistan onsuzda qrupda var🙄</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔵 Vaxt aşımı xətası 🔵\n User {user.first_name} Userbot çoxlu qoşulma sorğularına görə qrupunuza qoşula bilmədi! Köməkçinin qrupda qadağan edilmədiyinə əmin olun."
            "\n\n Yada asistan hesabını qrupa özün əlavə et </b>",
        )
        return
    await message.reply_text(
            "<b>Asistan onsuzda qrupda var🙄</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayril", "asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>İstifadəçi qrupunuzdan ayrılamadı!."
            "\n\nYada özün çıxara bilərsən</b>",
        )
        return
 
 
 
