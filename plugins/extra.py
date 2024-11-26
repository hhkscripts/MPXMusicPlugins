import requests
import nekos

from googlesearch import search
from pyrogram import filters
from TheApi import api
from MPXMusic import app

# Advice
@app.on_message(filters.command("advice"))
async def advice(_, message):
    A = await message.reply_text("...")
    res = await api.get_advice()
    await A.edit(res)

# Joke
@app.on_message(filters.command("joke"))
async def get_joke(_, message):
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=political"
    )
    r = response.json()
    joke_text = r["setup"]
    await message.reply_text(joke_text)

bored_api_url = "https://apis.scrimba.com/bored/api/activity"

# Bored
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

# Generate QR
@app.on_message(filters.command(["qr"]))
async def write_text(client, message):
    if len(message.command) < 2:
        await message.reply_text("**Usage**\n:- `/qr https://t.me/HeinHtetKyaw`")
        return
    text = " ".join(message.command[1:])
    photo_url = "https://apis.xditya.me/qr/gen?text=" + text
    await app.send_photo(
        chat_id=message.chat.id, photo=photo_url, caption="Here is your qrcode"
    )

# Google
@app.on_message(filters.command(["google", "gle"]))
async def google(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("Example:\n\n`/google lord ram`")
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])
    b = await message.reply_text("**Sᴇᴀʀᴄʜɪɴɢ ᴏɴ Gᴏᴏɢʟᴇ....**")
    try:
        a = search(user_input, advanced=True)
        txt = f"Search Query: {user_input}\n\nresults"
        for result in a:
            txt += f"\n\n[❍ {result.title}]({result.url})\n<b>{result.description}</b>"
        await b.edit(
            txt,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await b.edit(e)

# Slap
@app.on_message(filters.command("slap"))
async def slap(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(
                nekos.img("slap"),
                caption=f"{message.from_user.mention} sʟᴀᴘᴘᴇᴅ {message.reply_to_message.from_user.mention}",
            )
        else:
            await message.reply_video(nekos.img("slap"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")



__MODULE__ = "Exᴛʀᴀ"
__HELP__ = """
/advice - Gᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ.
/bored - Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ.
/joke - Gᴇᴛs ʀᴀɴᴅᴏᴍ Jᴏᴋᴇs.
/quiz - Gᴇᴛs ʀᴀɴᴅᴏᴍ ǫᴜɪᴢ.

/qr - Gᴇᴛs Gᴇɴᴇʀᴀᴛᴇᴅ QR.

/google [ǫᴜᴇʀʏ] - ᴛᴏ sᴇᴀʀᴄʜ ᴏɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ɢᴇᴛ ʀᴇsᴜʟᴛs.

/cat - Gᴇᴛ A Cᴀᴛ Aɴɪᴍᴀᴛɪᴏɴ.
/dog - Gᴇᴛ A Dᴏɢ Aɴɪᴍᴀᴛɪᴏɴ.
/hug - Gᴇᴛ ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ. Iғ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴍᴇssᴀɢᴇ, ɪᴛ ᴍᴇɴᴛɪᴏɴs ᴛʜᴇ sᴇɴᴅᴇʀ ᴀɴᴅ ʀᴇᴄɪᴘɪᴇɴᴛ ᴏғ ᴛʜᴇ ʜᴜɢ.

/slap - Sʟᴀᴘs sᴏᴍᴇᴏɴᴇ. Iғ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, sʟᴀᴘs ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ.
"""