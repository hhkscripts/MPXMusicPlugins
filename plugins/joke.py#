import requests
from pyrogram import filters
from MPXMusic import app


@app.on_message(filters.command("joke"))
async def get_joke(_, message):
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=political"
    )
    r = response.json()
    joke_text = r["setup"]
    await message.reply_text(joke_text)
