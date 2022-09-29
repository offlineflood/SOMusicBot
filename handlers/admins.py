from asyncio.queues import QueueEmpty
from cache.admins import admins
from asyncio import sleep
from pyrogram import Client
from pyrogram.types import Message
from callsmusic import callsmusic
from pyrogram import filters

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


ACTV_CALLS = []

@Client.on_message(command(["pause"]) & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    a = await message.reply_text("⇛ Musiqi dayandırıldı..!\n\n💡 Musiqi dəvam edmək üçün /play əmrindən isdifadə edə bilərsiniz.")
    await sleep(3)
    await a.delete()
    


@Client.on_message(command(["resume"]) & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    a = await message.reply_text("⇛ Musiqi dəvam edir..!\n\n💡 Musiqini dayandırmaq üçün /end əmrindən isdifadə edə bilərsiniz.")
    await sleep(3)
    await a.delete()
    


@Client.on_message(command(["end"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = message.chat.id 
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("ℹ️ Hal-hazırda musiqi səsli söhbət'də davam edmir..!")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass
        await callsmusic.pytgcalls.leave_group_call(chat_id)
        await _.send_message(
            message.chat.id,
            "❌ Musiqi dayandırıldı..!\n\nℹ️ Səsli söhbətdən asisstantın bağlantısı kəsildi!")
    
@Client.on_message(command(["skip"]) & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        a = await message.reply_text("ℹ️ Sırada olan musiqi gözlərən musiqi yoxdur..!\n\n💡 /play əmri ilə səsli söhbətə musiqi əlavə edə bilərsiniz.")
        await sleep(3)
        await a.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
            
        a = await message.reply_text("➥ Növbəti musiqiyə keç...**")
        await sleep(3)
        await a.delete()

# Yetki Vermek için (ver) Yetki almak için (al) komutlarını ekledim.
# Gayet güzel çalışıyor. @ismiyev95 Tarafından Eklenmiştir. 
@Client.on_message(command("ver") & other_filters)
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("💡İstifadəçiyə musiqi botu əmrlərini isdifadə etməsi üçün yetkiləndirlməsi üçün maj yanıtlayın!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("✅ İstifadəçi yetkiləndi...")
    else:
        await message.reply("🔰 İstifadəçi yetkilidir!")


@Client.on_message(command("al") & other_filters)
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("ℹ️ İstifadəçinin Yetkisini almaq üçün mesajına yanıt verin.")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("🔰 İstifadəçi yetkisizdir!")
    else:
        await message.reply("✅ Yetkisi alındı!")


# Sesli sohbet için 0-200 arası yeni komut eklenmiş oldu. 
@Client.on_message(command(["ses"]) & other_filters)
@authorized_users_only
async def change_ses(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
       callsmusic.pytgcalls.change_volume_call(chat_id, volume=int(range))
       await message.reply(f"✅ **Birim olaraq ayarlandı:** ```{range}%```")
    except Exception as e:
       await message.reply(f"**xəta:** {e}")

@Client.on_message(command("reload") & other_filters)
@errors
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await client.send_message(
        message.chat.id,
        "✅ **Bot yenidən başladı!**\n✅ **Admin siyahısı yeniləndi!**"
    )
