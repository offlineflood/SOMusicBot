from pyrogram import Client
import asyncio
from config import SUDO_USERS
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Salam 🗣, Musiqi asistanı xidmətidir.botla bağlı @WerabliAnlar\n\n ❗️ qaydalar:\n - Sohbete icazə yoxdu.\n - məlumat ve Menyularım üçün qrubun sohbetinde **/bilgi** yazsanız. (Asistan sohbetinə bilgi yazmayın.) Musiqi menyularını öyrənə bilərsiniz. \n - İstənməyən postaya icazə verilmez \n\n 🚨 **Userbot Qrupunuza Qoşulmursa >> DƏVƏT QOŞULMA ÖZƏLLİYİ VE SƏS YÖNƏTİMİ ÖZƏLLİKLƏRİ VER YÖNETİCİ EDİN. <<**\n\n ⚠️ DİQQƏT: Burada bir mesaj göndərsəniz. Yöneticinin iletinizi göreceyi anlamına gəlir.\n - Şəxsi bilgiləri burada paylaşmayın. (Musiqi Botunu Xaiş Edirik Gizli Qrublara almayın.) 📚 Bilgi üçün [Sahibim 👨🏻‍💻](https://t.me/ismiyev95) 🇦🇿\n",
            )
            return
 
    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("PM İzin Etkin")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("PM İzin Devre Dışı")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**Hey Userbot Yazışması artıq işləyir.**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Yaklaşık olarak PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Bu şekilde PM")
        return
    message.continue_propagation()
