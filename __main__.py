import asyncio

from pyrogram import Client, filters

from config import api_id, api_hash, love_text
from heart_generate import generate_heart


app = Client(
    "heart_bot",
    api_id=api_id,
    api_hash=api_hash
    )

@app.on_message(filters.me and filters.command("heart", "+"))
async def heart_animation(client, message):

    original_heart_lines = await generate_heart()
    heart_lines = original_heart_lines.split("\n")

    # copyright
    msg = await message.edit("Скрипт сделан fazzyt :3")

    # Полная отрисовка сердца
    for i in range(1, len(heart_lines) + 1):
        animated_heart = "\n".join(heart_lines[:i])
        await msg.edit(animated_heart)
        await asyncio.sleep(0.25)

    # Переливание
    for i in range(12):  
        heart_lines = await generate_heart()  
        await msg.edit(heart_lines)
        await asyncio.sleep(0.25)

    # Отображение текста
    current_text = "" 
    for word in love_text.split():
        current_text += word + " "
        await msg.edit(current_text.strip())
        await asyncio.sleep(0.25)
    

app.run()