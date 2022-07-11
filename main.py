from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Добро пожаловать на шоу {message.from_user.full_name}")


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"/start, /mem, /quiz, /help")


@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    stick = open('media/1.webp', 'rb')
    await bot.send_sticker(message.chat.id, sticker=stick)


@dp.message_handler(commands=['quiz'])
async def quest_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Какой псевдоним у Marshall Marshall Bruce Mathers III?"
    answers = [
        'Snoop Dog', "50 CENT", "Jay-Z", "Eminem"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Ты не шаришь в музыке",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )



@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quest_1(call: types.CallbackQuery):
    question = "Сколько месяцев в високосном году?"
    answers = [
        '11',
        '12',
        '13',
        '11.5',
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Даже люди Древнего Майя знают этот ответ",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )



@dp.message_handler()
async def echo(message: types.Message):
    try:
        i = int(message.text)
        await bot.send_message(message.from_user.id, i*i)
    except:
        await bot.send_message(message.from_user.id, message.text)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)