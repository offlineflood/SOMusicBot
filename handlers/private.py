from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/0a4f06f27de1ae61784fa.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli söhbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yetkisi verib, Asistanı qrupa əlavə edin.\n\nSahibim👉  [𓄂𝙰𝚂𝙾🇦🇿 『᭙Ҩ』❉͜͡➣ࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩ🦁𝕋𝕚𝔾𝕣](https://t.me/ismiyev95)**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/ASOMusicBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/ASOmusic_asisstant1"
                    ),
                    InlineKeyboardButton(
                        "Əyləncə 💬", url="https://t.me/WerabliAnlar"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿", url=f"https://t.me/ASOresmi"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Qeyd:\n Botun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli səhbəti yönətmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 İstifatəçi Əmrləri", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Admin  Əmrləri", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Geri 🔄", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "Owner 🇦🇿", url="https://t.me/ismiyev95")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Qeyd:\nBotun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️\n- Mesaj silmə yetkisi.\n- Bağlantı ilə dəvət etmə yetkisi.\n- Səsli söhbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨ Hərkəs üçün əmrlər", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑 Admin əmrləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "Owner 🇦🇿", url="https://t.me/ismiyev95")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün əmr menyusu 😉\n\n ▶️ /play - Musiqi oxutmaq üçün youtube url'sinə vəya musiqi faylına yanıt verin\n 🎵 /bul - İstədiyiniz musiqi sürətli bir şəkildə axtarın\n 🎵 /vbul - İstədiyiniz videoları sürətli bir şəkildə axtarın\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Owner 🇦🇿", url="https://t.me/ismiyev95")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün əmr menyusu 🤩\n\n ▶️ /resume - Musiqi oxutmağa davam et\n ⏸️ /end - Oxuyan musiqini dayandır\n 🔄 /skip - Sıraya alınmış musiqiyə keç\n 🔼 /promote - Botun sadəcə yönətici üçün olan əmrlərini istifadə üçün istifadəçiyə yetki ver\n 🔽 /demote - Botun yönətici əmrlərini istifadə edən istifadəçinin yetkisini al\n\n ⚪ /asistan - Musiqi asistanı qrupunuza qoşulur.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Owner 🇦🇿", url="https://t.me/ismiyev95")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yönətim yetki verib, Asistanı qrupa əlavə edin.\n\nSahibim👉  [𓄂𝙰𝚂𝙾🇦🇿 『᭙Ҩ』❉͜͡➣ࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩࠩ🦁𝕋𝕚𝔾𝕣](https://t.me/ismiyev95)**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/ASOMusicBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/ASOmusic_asisstant1"
                    ),
                    InlineKeyboardButton(
                        "Əyləncə 💬", url="https://t.me/WerabliAnlar"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿", url=f"https://t.me/ASOresmi"
                    )
                ]
                
           ]
        ),
    )
