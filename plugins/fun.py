import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from MPXMusic import app


@app.on_message(
    filters.command(
        [
            "dice",
            "ludo",
            "dart",
            "basket",
            "basketball",
            "football",
            "slot",
            "bowling",
            "jackpot",
        ]
    )
)
async def dice(c, m: Message):
    command = m.text.split()[0]
    if command == "/dice" or command == "/ludo":
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔄", callback_data="send_dice")]]
        )
        value = await c.send_dice(m.chat.id, reply_markup=keyboard)

    elif command == "/dart":

        value = await c.send_dice(m.chat.id, emoji="🎯", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

    elif command == "/basket" or command == "/basketball":
        basket = await c.send_dice(m.chat.id, emoji="🏀", reply_to_message_id=m.id)
        await basket.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(basket.dice.value))

    elif command == "/football":
        value = await c.send_dice(m.chat.id, emoji="⚽", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

    elif command == "/slot" or command == "/jackpot":
        value = await c.send_dice(m.chat.id, emoji="🎰", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))
    elif command == "/bowling":
        value = await c.send_dice(m.chat.id, emoji="🎳", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))


@app.on_callback_query(filters.regex(r"send_dice"))
async def dice_again(client, query):
    try:
        await app.edit_message_text(
            query.message.chat.id, query.message.id, query.message.dice.emoji
        )
    except BaseException:
        pass
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔄", callback_data="send_dice")]]
    )
    await client.send_dice(query.message.chat.id, reply_markup=keyboard)


__MODULE__ = "Fᴜɴ"
__HELP__ = """
**ʜᴀᴠɪɴɢ ꜰᴜɴ:**

• `/dice`: Rᴏʟʟs ᴀ ᴅɪᴄᴇ.
• `/ludo`: Pʟᴀʏ Lᴜᴅᴏ.
• `/dart`: Tʜʀᴏᴡs ᴀ ᴅᴀʀᴛ.
• `/basket` ᴏʀ `/basketball`: Pʟᴀʏs ʙᴀsᴋᴇᴛʙᴀʟʟ.
• `/football`: Pʟᴀʏs ғᴏᴏᴛʙᴀʟʟ.
• `/slot` ᴏʀ `/jackpot`: Pʟᴀʏs ᴊᴀᴄᴋᴘᴏᴛ.
• `/bowling`: Pʟᴀʏs ʙᴏᴡʟɪɴɢ.
• `/bored`: Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ ɪғ ʏᴏᴜ'ʀᴇ ʙᴏʀᴇᴅ.
"""
