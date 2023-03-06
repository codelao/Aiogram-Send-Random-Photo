from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


Menu = InlineKeyboardMarkup(row_width=1)
btnGetPhoto = InlineKeyboardButton(text='📍Get random photo from Bing', callback_data='GetPhoto')
Menu.add(btnGetPhoto)
