import aiogram
from decouple import config

TOKEN = config('TOKEN')
bot = aiogram.Bot(TOKEN)
dp = aiogram.Dispatcher(bot=bot)