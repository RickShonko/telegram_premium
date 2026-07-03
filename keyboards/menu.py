from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💳 Subscribe")
        ],
        [
            KeyboardButton(text="ℹ️ About"),
            KeyboardButton(text="❓ Help")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose an option..."
)