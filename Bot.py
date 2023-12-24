from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


bot = Bot(token='6989292153:AAERB7SBBhJErrUCTcjp0zZHdjudQgNanGk')
dp = Dispatcher(bot)

@dp.message_handler(commands=('start'))
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["/меню", "/проект"]
    keyboard.add(*buttons)
    await message.reply("Здраствуйте,это демонстрация телеграмм бота\nсделанного на Python с библиотекой Aiogram\n доступные сейчас комнды:",reply_markup=keyboard)

@dp.message_handler(commands=('меню'))
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["/проект"]
    keyboard.add(*buttons)
    await message.reply("Нажмите кнопку /проект и получите ссылку на презентацию\nи несколько документаций и код этого бота",reply_markup=keyboard)

@dp.message_handler(commands=('проект'))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Презентация',url='https://docs.google.com/presentation/d/1oUrqn4LTkgMyzFMq0U_xLirfWr170a5E/edit?usp=sharing&ouid=110137944540007182069&rtpof=true&sd=true')
    button2 = InlineKeyboardButton('Документация \nAiogram', url='https://aiogram.dev/')
    button3 = InlineKeyboardButton('Документация \nPython', url='https://www.python.org/')
    button4 = InlineKeyboardButton('Код бота', url='https://github.com/username234dw/bot_aiogam2')
    keyboard.add(button,button2,button3,button4)
    await message.reply("Все ссылки ниже.",reply_markup=keyboard)
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["/меню","/start"]
    key.add(*buttons)
    await message.reply("Так же вы можете нажать кнопку меню и вернуться в меню\n либо перезапусить бота /stаrt.",reply_markup=key)
@dp.message_handler()
async def echo(message: types.Message):
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["/меню", "/start"]
    key.add(*buttons)
    await message.reply("Такой команды не существует\nвы можете нажать кнопку меню и вернуться в меню\n либо перезапусить бота /stаrt.",reply_markup=key)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)