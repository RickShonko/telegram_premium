from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "💳 Subscribe")
async def subscribe(message: Message):
    await message.answer(
        "💎 Premium Membership\n\n"
        "KES 500 / Month\n\n"
        "✔ Access Premium Group\n"
        "✔ Exclusive Content\n"
        "✔ Priority Support\n\n"
        "💳 Payment integration coming in the next episode..."
    )


@router.message(lambda message: message.text == "ℹ️ About")
async def about(message: Message):
    await message.answer(
        "🤖 Premium Bot\n\n"
        "This bot helps creators manage paid Telegram communities automatically.\n\n"
        "Built with Python and aiogram."
    )


@router.message(lambda message: message.text == "❓ Help")
async def help_command(message: Message):
    await message.answer(
        "❓ Need Help?\n\n"
        "Contact:\n"
        "@yourusername"
    )