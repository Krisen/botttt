import asyncio
import logging
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7093391074:AAEh_LxTz5gi6rwFzHXGJ4u7LLCBELD0-Qg")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_special_buttons(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True),
    )
    await message.answer(
        "Отправь геолокацию",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

locations = {}

@dp.message(F.location)
async def location_handler(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    locations['latitude'] = latitude
    locations['longitude'] = longitude
    print(latitude)
    print(longitude)
    await message.answer(
        f"долгота - {latitude}, ширина - {longitude}",

    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main())