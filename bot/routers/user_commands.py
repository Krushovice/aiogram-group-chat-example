from aiogram import Router

from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router(name=__name__)


@router.message()
async def echo_command(message: Message):

    await message.answer(message.text)
