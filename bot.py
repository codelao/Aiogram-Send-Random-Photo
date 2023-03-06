import markups as nav
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Hi!", reply_markup=nav.Menu)

      
@dp.callback_query_handler(text='GetPhoto')
async def getphoto(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=types.InputFile.from_url("https://bing.ioliu.cn/v1/rand"))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
