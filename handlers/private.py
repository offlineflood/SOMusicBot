from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/6e7d20219471595061042.jpg",
                caption=(f"""**Salam {message.from_user.mention}. Mənim adım [𝐒𝐎 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🇦🇿](https://t.me/SOmusiqi_Bot)\n\nℹ️Mənim {bot} bəzi faydalı xüsusiyyətləri olan teleqram musiqi botuyam.iQrup'lara əlavə edərək musiqi dinləyə bilərsiniz.\n\n⚡️Məni qruplarınıza əlavə etməkdən çəkinməyin.**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕Qrupa Əlavə Et➕", url=f"https://t.me/SOmusiqi_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Əmrlər 📚", callback_data= "cbbilgi"
                    ),
                    #InlineKeyboardButton(
                    #    "📑 Təkliflər", url="https://t.me/emrelguseynovv"
                   # )
                ],
 #               [
  #                  InlineKeyboardButton(
   #                     "Sahib💥", url="https://t.me/emrelguseynovv"
    #                )
     #           ],
                 [
                    InlineKeyboardButton(
                        "Sahib💥", url="https://t.me/emrelguseynovv"
                    ),
                    InlineKeyboardButton(
                        "Qrup 💬" , url="https://t.me/SohbetOnlineAz"
                    )
                ]
                
           ]
        )
    )
  


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("**Bot'un Əmrlər üçün?.Bot'a daxil olub.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "↬Bota Get↫", url="https://t.me/SOmusiqi_Bot?start=start"),                     
                     InlineKeyboardButton(
                         "📑 Təkliflər", url="https://t.me/emrelguseynovv")
                 ],[
                     InlineKeyboardButton(
                         "➕Qrupa Əlavə Et➕", url=f"https://t.me/SOmusiqi_Bot?startgroup=true")
                 ]
             ]
         )
    )
    
#**Salam {message.from_user.mention}. Mənim adım [𓆩𓄂𝙰𝚂𝚀🇦🇿 ᴍᴜsiᴄ ʙᴏᴛ🎶](https://t.me/Ustamusicbot)\n\nℹ️Mənim {bot} bəzi faydalı xüsusiyyətləri olan teleqram musiqi botuyam. @ustabots-dan dəsdək alaraq yaradılmışam. Qrup'lara əlavə edərək musiqi dinləyə bilərsiniz.\n\n⚡️Məni qruplarınıza əlavə etməkdən çəkinməyin.   
@Client.on_callback_query(filters.regex("herkess"))
async def herkess(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {message.from_user.mention}. Mənim adım [𝐒𝐎 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🇦🇿](https://t.me/SOmusiqi_Bot)\n\nℹ️Mənim {bot} bəzi faydalı xüsusiyyətləri olan teleqram musiqi botuyam. @ustabots-dan dəsdək alaraq yaradılmışam. Qrup'lara əlavə edərək musiqi dinləyə bilərsiniz.\n\n⚡️Məni qruplarınıza əlavə etməkdən çəkinməyin.""",
    reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("➕Qrupa Əlavə Et➕", url=f"https://t.me/SOmusiqi_Bot?startgroup=true" )],
             [InlineKeyboardButton("Əmrlər 📚", callback_data= "cbbilgi")],
            # [InlineKeyboardButton("Sahib💥", url="https://t.me/emrelguseynovv")],
             [InlineKeyboardButton("Sahib💥", url="https://t.me/emrelguseynovv")],]))
              InlineKeyboardButton("Qrup 💬" , url="https://t.me/SohbetOnlineAz")]]))    
   
@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("ℹ️Bot səsdə musiqi oxuması üçün lazım olan yetkilər.\n\n\n•━━━━━━━━•••━━━━━━━━•\n✅Mesaj Silmə.\n✅Bağlantı ilə dəvət etmə.\n✅Səsli söhbəti yönətmə.\n•━━━━━━━━•••━━━━━━━━•", 
    reply_markup=InlineKeyboardMarkup(
      [[InlineKeyboardButton("Bot Əmrləri🤖",callback_data ="herkes"),
         InlineKeyboardButton("Admin Əmrləri👮",callback_data ="admin")],
        [InlineKeyboardButton("◀️Geri", callback_data="herkess")]])) 


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b> {query.from_user.mention} Bot Əmrləri🤖' Əmrlər aşağıda qeyid olunub⚡️\n\n\n•━━━━━━━━•••━━━━━━━━•\n/play - Qrupda musiqi oxutmaq üçün isdifadə olunan əmr.\n\n/song - İstədiyiniz musiqi adı ve ya bi hissəsin yazın, mp3 şəkildə musiqi yükləmək üçün isdifadə olunan əmr.\n\n/download - İstədiyiniz video adı ve ya bi hissəsin yazın, mp4 şəkildə video yükləmək üçün isdifadə olunan əmr.\n\n/link - Link şəkildə musiqi axtarmaq üçün lazım olan əmr.\n\n/help - Qrup & Şəxsidə əmrlər üçün lazım olan əmr.\n\n/id - Qrup & Şəxs id.\n\n/leave - Asisstant hesabı qrupdan çıxarmaq üçün isdifadə olunan əmr.</b>""",
    reply_markup=InlineKeyboardMarkup(
             [[InlineKeyboardButton("️◀️Geri",callback_data="cbbilgi")]]))


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b> {query.from_user.mention}'Admin Əmrləri👮' Ərmlər aşağıda qeyid olunub⚡️\n\n\n•━━━━━━━━•••━━━━━━━━•\n/authority - İstifadəçinin botun 'Admin Əmrləri👮' əmrlərindən istifadə edmə yetkisini ver.\n\n/unauthorized - İstifadəçinin botun 'Admin Əmrləri👮' əmrlərindən istifadə edmə yetkisini al.\n\n/skip - Sırada gözləyən musiqi oynatmaqa başlat.\n\n/resume - Musiqini oxutmağa davam edir.\n\n/end - Oxuyan musiqini dayandır.\n\n/adding - Asisstant hesabı qrupa qoşmaq üçün, lazım olan əmr.\n\n/reload - Botu yenidən başlad.</b>""",
    reply_markup=InlineKeyboardMarkup(
             [[InlineKeyboardButton("️◀️Geri", callback_data="cbbilgi")]]))
    
    
