

from aiogram import Router

from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router(name=__name__)


@router.message(CommandStart())
async def start_command(message: Message):
    txt = f"Приветствую {message.from_user.first_name} в нашем сообществе книголюбов!🖖🏻"

    await message.answer(txt)