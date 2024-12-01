import asyncio

from pyrogram import Client, filters

from config import api_id, api_hash
from heart_generate import generate_heart


app = Client(
    "heart_bot",
    api_id=api_id,
    api_hash=api_hash
    )

@app.on_message(filters.me and filters.command("heart", "+"))
async def heart_animation(client, message):
    heart_lines = await generate_heart()
    heart_lines = heart_lines.split("\n")
    
    # Полная отрисовка сердца
    for i in range(1, len(heart_lines) + 1):
        animated_heart = "\n".join(heart_lines[:i])
        await message.edit(animated_heart)
        await asyncio.sleep(0.25)

    # Переливание
    for i in range(12):  
        heart_lines = await generate_heart()  
        await message.edit(heart_lines)

        await asyncio.sleep(0.25)
    

app.run()