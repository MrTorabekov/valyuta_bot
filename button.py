from aiogram.types import ReplyKeyboardMarkup,KeyboardButton , InlineKeyboardButton,InlineKeyboardMarkup

enter1 = [
    [KeyboardButton(text="RUB"),    KeyboardButton(text="UZS")],
    [KeyboardButton(text="Boshqa")]
]

enter2 = ReplyKeyboardMarkup(keyboard=enter1,resize_keyboard=True)

Other = [
    [KeyboardButton(text="PLN"),KeyboardButton(text="KZT")]
]

Other2 = ReplyKeyboardMarkup(keyboard=Other,resize_keyboard=True)
# Other = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="PLN",callback_data="pln") , InlineKeyboardButton(text="KZT",callback_data="kzt")]
# ])