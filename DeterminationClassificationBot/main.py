import asyncio
import logging
import sys
from typing import BinaryIO
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, BufferedInputFile

from config import TOKEN
from ai import predict

dp: Dispatcher = Dispatcher()
_ANSWER_IMAGE_FILENAME: str = 'answer.jpg'


@dp.message(F.photo)
async def photo_handler(message: Message) -> None:
    file_id: str = message.photo[-1].file_id
    image_io: BinaryIO = await message.bot.download(file=file_id)

    answer_image_bytes, class_ = predict(image_bytes=image_io.read())

    photo: BufferedInputFile = BufferedInputFile(image_io.read(), _ANSWER_IMAGE_FILENAME)
    caption: str = f'Класс: {class_}'

    await message.answer_photo(photo, caption=caption)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
