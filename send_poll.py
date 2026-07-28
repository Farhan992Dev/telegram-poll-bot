import os
import json
import asyncio
import random
from datetime import datetime

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


def load_questions():
    with open("questions.json", "r", encoding="utf-8") as f:
        return json.load(f)


def get_random_question():
    return random.choice(load_questions())


async def send_poll():
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    if not bot_token or not chat_id:
        raise ValueError("BOT_TOKEN and CHAT_ID environment variables required")

    question = get_random_question()

    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    try:
        await bot.send_poll(
            chat_id=int(chat_id),
            question=question["text"],
            options=question["options"],
            is_anonymous=False,
            allows_multiple_answers=question.get("multiple_choice", True),
            type="regular"
        )
        print(f"[{datetime.now()}] Poll sent: {question['text'][:50]}...")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(send_poll())