import requests
import nekos

from pyrogram import filters
from TheApi import api
from MPXMusic import app


@app.on_message(filters.command("advice"))
async def advice(_, message):
    A = await message.reply_text("...")
    res = await api.get_advice()
    await A.edit(res)

@app.on_message(filters.command("joke"))
async def get_joke(_, message):
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=political"
    )
    r = response.json()
    joke_text = r["setup"]
    await message.reply_text(joke_text)

bored_api_url = "https://apis.scrimba.com/bored/api/activity"


@app.on_message(filters.command("bored"))
async def bored_command(client, message):
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity")
        if activity:
            await message.reply(f"{activity}")
        else:
            await message.reply("Nᴏ ᴀᴄᴛɪᴠɪᴛʏ ғᴏᴜɴᴅ.")
    else:
        await message.reply("Fᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴀᴄᴛɪᴠɪᴛʏ.")

@app.on_message(filters.command("hug"))
async def huggg(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(
                nekos.img("hug"),
                caption=f"{message.from_user.mention} hugged {message.reply_to_message.from_user.mention}",
            )
        else:
            await message.reply_video(nekos.img("hug"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")


__MODULE__ = "Iᴅᴇᴀs"
__HELP__ = """
/advice - Gᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ.
/bored - Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ.
/joke - Gᴇᴛs ʀᴀɴᴅᴏᴍ Jᴏᴋᴇs.
/quiz - Gᴇᴛs ʀᴀɴᴅᴏᴍ ǫᴜɪᴢ.

/cat - Gᴇᴛ A Cᴀᴛ Aɴɪᴍᴀᴛɪᴏɴ.
/dog - Gᴇᴛ A Dᴏɢ Aɴɪᴍᴀᴛɪᴏɴ.
/hug: Gᴇᴛ ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ. Iғ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴍᴇssᴀɢᴇ, ɪᴛ ᴍᴇɴᴛɪᴏɴs ᴛʜᴇ sᴇɴᴅᴇʀ ᴀɴᴅ ʀᴇᴄɪᴘɪᴇɴᴛ ᴏғ ᴛʜᴇ ʜᴜɢ.
"""