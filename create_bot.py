from aiogram import Dispatcher, Bot
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

ID = int(os.getenv('ID'))
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
