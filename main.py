from aiogram import Bot, Dispatcher, executor, types
from background import keep_alive
from aiogram import *
from aiogram.utils.markdown import hlink
from aiogram.types import *
from aiogram import types
from aiogram.dispatcher.filters import Text

TOKEN = "example"  # Токен бота
admin_id = 1111111  # ИД админа (узнать можно в боте @username_to_id_bot )

boty = Bot(token=TOKEN)
dp = Dispatcher(boty)


@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

  buttons_row1 = ["🧐Предложения"]
  buttons_row2 = ["⚡️Крутки", "🎬Видео"]
  buttons_row3 = ["💫Поддержка"]
  buttons_row4 = ["🎥Ссылки на меня"]  

  keyboard.add(*buttons_row1)
  keyboard.add(*buttons_row2)
  keyboard.add(*buttons_row3)
  keyboard.add(*buttons_row4)  

  await message.answer(
      f"Привет {message['from'].first_name}👋!\n \nЯ - ЛОХБОТ❤️\nМой хозяин меня не уважает🥲\nНо я могу помочь вам в контакте по поводу всяких важных штуковин \n \nТыкай на кнопки ниже! 👇 \n \n \n Спасите...",
      reply_markup=keyboard)


@dp.message_handler(Text(equals="⚡️Крутки"))
async def with_puree(message: types.Message):

  await message.reply(
      'Заполни форму\nhttps://forms.gle/pLUhLLX5KnSPZjvCA\nИ обязательно напиши об этом сюда, как отправишь ее.\n \n \nслушайся, пожалуйста, иначе меня опять ударят'
  )


@dp.message_handler(Text(equals="💫Поддержка"))
async def with_puree(message: types.Message):
  await message.reply(
      "🍃 Арты(рисунки)\n🍃Набор модераторов (если объявили, что надо)\n🍃Ты не нашел в прошлых кнопках то, что искал\n🍃Что то важное\n \n \n...не спамь тут по личным вопросам, иначе меня закроют в чулане, а тебя забанят...⛔️😰"
  )


@dp.message_handler(Text(equals="🧐Предложения"))
async def process_start_command(message: types.Message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = [
      "💡Предложения о творчестве", "💸Предложения о сотрудничестве",
      "🔁Вернуться в меню"
  ]

  for button in buttons:
    keyboard.add(button)

  await message.answer("Выбирай", reply_markup=keyboard)


@dp.message_handler(Text(equals="💡Предложения о творчестве"))
async def with_puree(message: types.Message):
  await message.reply(
      "Любые предложения и идеи на счет:\n \n🍀Видео \n🍀ТГ канала\n🍀Стримов\n🍀Контента\n \nИ в целом творчества Лохуфи🙈\n \nМожешь написать мне сюда, я постараюсь договорится с ним о реалзации🫡\n \n \n...надеюсь тут что-то интересное, хочу вспомнить какого быть без синяков...🤕"
  )


@dp.message_handler(Text(equals="💸Предложения о сотрудничестве"))
async def with_puree(message: types.Message):
  await message.reply(
      "Предложения финансового характера пиши сюда.👇\n \n⭐️ Реклама в ТГ канале/Ютубе/ТикТоки другие соц сети.\n \n⭐️ Любые взаимодействия и проекты с участием loxyfi, которые содержат материальный характер.\n \n \n \n...спасибо тебе, добрый человек, надеюсь он меня покормит...🥹"
  )


@dp.message_handler(Text(equals="🔁Вернуться в меню"))
async def process_start_command(message: types.Message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

  buttons_row1 = ["🧐Предложения"]
  buttons_row2 = ["⚡️Крутки", "🎬Видео"]
  buttons_row3 = ["💫Поддержка"]
  buttons_row4 = ["🎥Ссылки на меня"]  

  keyboard.add(*buttons_row1)
  keyboard.add(*buttons_row2)
  keyboard.add(*buttons_row3)
  keyboard.add(*buttons_row4)  

  await message.answer(
      f"Привет {message['from'].first_name}👋!\n \nЯ - ЛОХБОТ❤️\nМой хозяин меня не уважает🥲\nНо я могу помочь вам в контакте по поводу всяких важных штуковин \n \nТыкай на кнопки ниже! 👇 \n \n \n Спасите...",
      reply_markup=keyboard)


@dp.message_handler(Text(equals="🎬Видео"))
async def with_puree(message: types.Message):
  await message.reply(
      "Если ты тут, то тебя попросили написать!😑\n \nНе забудь оставить ссылку на себя\n \n \n \nВ перспективе взаимодействия и игры🏆\n \nИ для этого нужны будут добровольцы на участие в видео.\nТак же буду использовать эту плашку в будущем для творческого контакта с вами и набора людей.🤫"
  )


@dp.message_handler(lambda message: message.text == "🎥Ссылки на меня")
async def process_links_button(message: types.Message):
  # Inline keyboard with links
  inline_keyboard = types.InlineKeyboardMarkup(row_width=2)

  youtube_button = types.InlineKeyboardButton(
      "YouTube 📹",
      url="https://www.youtube.com/channel/UCf09OSt2gfS9KUMyOfltFiw")
  tiktok_button = types.InlineKeyboardButton(
      "TikTok 🐣", url="https://www.tiktok.com/@loxyfi?_t=8fUlQGEsHR3&_r=1")
  chat_button = types.InlineKeyboardButton(
      "Чат 🐾", url="https://t.me/+lIL8cEahp4RkMWEy")
  channel_button = types.InlineKeyboardButton("ТГ Канал 🍄",
                                              url="https://t.me/loxyfi")
  discord_button = types.InlineKeyboardButton(
      "Discord 👾", url="https://discord.gg/s32D5RfK")
  twitch_button = types.InlineKeyboardButton(
      "Twitch 🌵", url="https://www.twitch.tv/loxyfi")
  donate_button = types.InlineKeyboardButton(
      "Донаты 💸", url="https://www.donationalerts.com/r/loxyfi")

  inline_keyboard.add(youtube_button, tiktok_button, chat_button,
                      channel_button, discord_button, twitch_button,
                      donate_button)

  await message.answer("ПОДПИСЫВАЙСЯ НА МЕНЯ ТУТ 🦋",
                       reply_markup=inline_keyboard)


@dp.message_handler()
async def process_start_command(message: types.Message):
  if message.reply_to_message == None:
    if '/start' not in message.text:
      await boty.forward_message(
          admin_id,
          message.from_user.id,
          message.message_id,
      )
      await message.answer('Спасибо за инициативу, с тобой свяжутся!💕')
  else:
    if message.from_user.id == admin_id:
      if message.reply_to_message.forward_from:
        await boty.send_message(message.reply_to_message.forward_from.id,
                                message.text)
    else:
      await boty.forward_message(
          admin_id,
          message.from_user.id,
          message.message_id,
      )
      await message.answer('Дополняю сообщение, с тобой свяжутся!💕')


@dp.message_handler(content_types=['photo'])  # повторение, только с фото
async def handle_docs_photo(message):
  await boty.forward_message(admin_id, message.from_user.id,
                             message.message_id)
  await message.answer('Ого, даже так... Передал админу!')


@dp.message_handler(content_types=['document'])  # тут с файлом
async def handle_docs_photo(message):
  await boty.forward_message(admin_id, message.from_user.id,
                             message.message_id)
  await message.answer('Файлик? Спасибо, передал админу)')


keep_alive()

if __name__ == '__main__':
  print("starting")
  executor.start_polling(dp)
