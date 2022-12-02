import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink

from auth import token
from main import collect_data
from Kognac import collect_data_k
from rom import collect_data_r
from vermut import collect_data_v


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ["🥃 Вискарь", "🍷 Коньяк", "🍹 Ром", "🍸 Вермут"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*start_buttons)

    await message.answer("Алкашка со скидкой", reply_markup=keyboard)


@dp.message_handler(Text(equals="🥃 Вискарь"))
async def get_discount_alko(message: types.Message):
    await message.answer("Загружаю, ждите...")

    collect_data()

    with open('response.json', 'r', encoding='utf-8') as file:
        for item in json.load(file):
            card = f"{hlink(item.get('title'), item.get('link'))}\n" \
                    f"{hbold('Производитель: ')}{item.get('subTitle')}\n" \
                    f"{hbold('Прайс: ')}{item.get('regularPrice')}\n" \
                    f"{hbold('Прайс со скидкой: ')}{item.get('cardPrice')}\n" \
                    f"{hbold('Процент скидки: ')}{item.get('product_promoPercent')}%\n"

            await message.answer(card)


@dp.message_handler(Text(equals="🍷 Коньяк"))
async def get_discount_alko(message: types.Message):
    await message.answer("Загружаю, ждите...")

    collect_data_k()

    with open('responsek.json', 'r', encoding='utf-8') as file:
        for item in json.load(file):
            card = f"{hlink(item.get('title'), item.get('link'))}\n" \
                    f"{hbold('Производитель: ')}{item.get('subTitle')}\n" \
                    f"{hbold('Прайс: ')}{item.get('regularPrice')}\n" \
                    f"{hbold('Прайс со скидкой: ')}{item.get('cardPrice')}\n" \
                    f"{hbold('Процент скидки: ')}{item.get('product_promoPercent')}%\n"

            await message.answer(card)


@dp.message_handler(Text(equals="🍹 Ром"))
async def get_discount_alko(message: types.Message):
    await message.answer("Загружаю, ждите...")

    collect_data_r()

    with open('responser.json', 'r', encoding='utf-8') as file:
        for item in json.load(file):
            card = f"{hlink(item.get('title'), item.get('link'))}\n" \
                    f"{hbold('Производитель: ')}{item.get('subTitle')}\n" \
                    f"{hbold('Прайс: ')}{item.get('regularPrice')}\n" \
                    f"{hbold('Прайс со скидкой: ')}{item.get('cardPrice')}\n" \
                    f"{hbold('Процент скидки: ')}{item.get('product_promoPercent')}%\n"

            await message.answer(card)


@dp.message_handler(Text(equals="🍸 Вермут"))
async def get_discount_alko(message: types.Message):
    await message.answer("Загружаю, ждите...")

    collect_data_v()

    with open('responsev.json', 'r', encoding='utf-8') as file:
        for item in json.load(file):
            card = f"{hlink(item.get('title'), item.get('link'))}\n" \
                    f"{hbold('Производитель: ')}{item.get('subTitle')}\n" \
                    f"{hbold('Прайс: ')}{item.get('regularPrice')}\n" \
                    f"{hbold('Прайс со скидкой: ')}{item.get('cardPrice')}\n" \
                    f"{hbold('Процент скидки: ')}{item.get('product_promoPercent')}%\n"

            await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
