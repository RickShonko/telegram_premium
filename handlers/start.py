from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.menu import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Welcome to Premium Bot!\n\n"
        "Choose an option below.",
        reply_markup=main_menu
    )