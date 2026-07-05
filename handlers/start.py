from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.menu import main_menu
from database.users import add_user

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    # Save the user to the database
    add_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name
    )

    # Send the welcome message
    await message.answer(
        "👋 Welcome to Premium Bot!\n\n"
        "Choose an option below.",
        reply_markup=main_menu
    )