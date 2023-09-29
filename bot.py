import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
