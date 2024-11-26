from pyrogram import filters
from TheApi import api
from MPXMusic import app


@app.on_message(filters.command("advice"))
async def advice(_, message):
    A = await message.reply_text("...")
    res = await api.get_advice()
    await A.edit(res)


__MODULE__ = "Exᴛʀᴀ"
__HELP__ = """
/advice - Gᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ.
/bored - Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ ɪғ ʏᴏᴜ'ʀᴇ ʙᴏʀᴇᴅ.
 quiz - ᴛᴏ ɢᴇᴛ ᴀɴ ʀᴀɴᴅᴏᴍ ǫᴜɪᴢ.
"""
