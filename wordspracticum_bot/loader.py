from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
TOKEN = '5329573655:AAGN2NlMR6Qib9h1w4nLUTUG9mxJ_ttKv68'


storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)