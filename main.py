import aiogram
from aiogram import *
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import *
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
import requests
import json
API_TOKEN = '6242731035:AAFYqXZFXvj-jz0ZZAU_4iLfzp8TvN47m0I'

admins = (
    1058211493, 
    777000
)


scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def get_updates():
    url = "https://api.telegram.org/bot<your_bot_token>/getUpdates"
    response = requests.get(url)
    data = json.loads(response.content)
    return data

def parse_message(data):
    try:
        message = data['result'][-1]['message']
        text = message['text']
        chat_id = message['chat']['id']
        return text, chat_id
    except KeyError:
        return None, None
async def start_notify(dp):
    await dp.bot.send_message(admins[0], "Бот запущен")

async def on_startup(dp):
    await start_notify(dp)




@dp.message_handler(content_types=['text'])
async def check(message: types.Message):
    chat_id = message.chat.id
    # message_text = message.reply_to_message.message_id
    message.reply_to_message.forward_sender_name
    await bot.send_message(chat_id, message.reply_to_message.forward_sender_name)
    # message = await message.get_messages(chat_id=chat_id, message_ids=message_text)
    # await bot.send_message(chat_id, message)
    # await bot.copy_message(chat_id, chat_id, message_text)
    message.bot
if __name__ == '__main__':
    
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
