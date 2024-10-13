from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from valyutalar import currencies
enter1 = [
    [KeyboardButton(text="RUB"),    KeyboardButton(text="UZS")],
    [KeyboardButton(text="USD"),    KeyboardButton(text="EUR")],
    [KeyboardButton(text="Boshqa")]
]

enter2 = ReplyKeyboardMarkup(keyboard=enter1,resize_keyboard=True)

# Har bir qator uchun maksimal tugma sonini belgilash
buttons_per_row = 3
Other = []

# Valyuta tugmalarini qatorlarga bo'lib oling
for i in range(0, len(currencies), buttons_per_row):
    row = [KeyboardButton(text=value) for value in list(currencies.values())[i:i + buttons_per_row]]
    Other.append(row)
Other2 = ReplyKeyboardMarkup(keyboard=Other,resize_keyboard=True)
