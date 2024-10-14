import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import requests
from button import enter2, Other2
from config import TOKEN

dp = Dispatcher()


class Form(StatesGroup):
    currency1 = State()  # fromCurrency
    currency2 = State()  # toCurrency
    amount = State()  # qiymat  # noqa
    finish = State()  # finish


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext,bot:Bot):
    await message.answer(f"Assalomu Aleykum botimizga xush kelibsiz, {message.from_user.mention_html()}")

    # @dp.message(Command("converter"))
    # async def cmd_converter(message: types.Message, state: FSMContext):
    await state.set_state(Form.currency1)
    await message.answer("Qaysi valyutani almashtirmoqchisiz?", reply_markup=enter2)

@dp.message(F.text == "Boshqa")
async def remove_button(message: types.Message,state: FSMContext,bot:Bot):
    await state.update_data(currency1=message.text)
    await state.set_state(Form.currency1)
    delete = await message.answer("Ozingizga kerakli valyutani tanlang!",reply_markup=ReplyKeyboardRemove())
    await bot.delete_message(chat_id=message.chat.id,message_id=delete.message_id)
    await message.answer("Qaysi valyutani almashtirmoqchisiz?", reply_markup=Other2)



@dp.message(Form.currency1)
async def currency1(message: types.Message, state: FSMContext):
    await state.update_data(currency1=message.text)
    await state.set_state(Form.currency2)
    await message.answer("Qaysi valyutaga?",reply_markup=Other2)


@dp.message(Form.currency2)
async def currency2(message: types.Message, state: FSMContext):
    await state.update_data(currency2=message.text)
    await state.set_state(Form.amount)
    await message.answer("Miqdorni kiriting: ")


@dp.message(Form.amount)
async def amount(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(amount=message.text)
    await state.set_state(Form.finish)
    delete = await message.answer("Biroz kuting ...")
    data = await state.get_data()
    await state.clear()
    currency1 = data.get("currency1", "Unknown")
    currency2 = data.get("currency2", "Unknown")
    amount = data.get("amount", "Unknown")

    url = "https://fast-currency-convertor.p.rapidapi.com/api/Fetch-Currency/"


    querystring = {"amount": f"{amount}", "fromCurrency": f"{currency1}", "toCurrency": f"{currency2}"}

    headers = {
        "X-RapidAPI-Key": "f8815dad22mshce0f3b4c90be0d3p1724ffjsndf9ebcee49ad",
        "X-RapidAPI-Host": "fast-currency-convertor.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = response.json().get("value")
    await bot.delete_message(chat_id=message.chat.id, message_id=delete.message_id)
    await bot.send_message(chat_id=message.chat.id, text=f"""
Qaysi valyutadan: {currency1}
Qaysi valyutga: {currency2}
Miqdori: {amount}
Natija: {result}
        """)
    await message.answer("Yana valyuta almashtirishni xohlaysizmi?", reply_markup=ReplyKeyboardRemove())

    # Yangi sessiyani boshlash
    await state.clear()  # State tozalash
    await state.set_state(Form.currency1)  # Boshidan boshlash uchun holatni yangilash
    await message.answer("Qaysi valyutani almashtirmoqchisiz?", reply_markup=enter2)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
