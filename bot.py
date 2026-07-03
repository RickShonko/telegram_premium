import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.menu import router as menu_router

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Register routers
dp.include_router(start_router)
dp.include_router(menu_router)


async def main():
    print("🤖 Bot is running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())