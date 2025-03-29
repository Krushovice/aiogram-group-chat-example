import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.config import settings

from core.routers import router as main_commands_router


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # Register all the routers from handlers package
    dp.include_routers(
        main_commands_router,
    )

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(
        token=settings.bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )

    # And the run events dispatching
    await dp.start_polling(bot)
    await bot.send_message(
        chat_id=int(settings.admin.admin),
        text="Бот запущен!",
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
