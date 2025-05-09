import os
import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from dotenv import load_dotenv
from api.api_client import TinkoffAPIClient

load_dotenv()

TOKEN = os.getenv("INVEST_TOKEN")
API_TOKEN = os.getenv("API_TOKEN")  # Укажите токен бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()  # Создаем маршрутизатор

# Инициализация API клиента
tinkoff_client = TinkoffAPIClient(token=TOKEN)

# Обработчик команды /start и /help
@router.message(F.text.in_({"/start", "/help"}))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который показывает данные о твоем портфеле. Используй команду /portfolio.")

# Обработчик команды /portfolio
@router.message(F.text == "/portfolio")
async def send_portfolio(message: types.Message):
    try:
        portfolio = tinkoff_client.get_portfolio()
        positions = portfolio.positions  # Получаем позиции из портфеля
        formatted_data = tinkoff_client.format_portfolio_data(positions)

        response = "Ваш портфель:\n\n" + formatted_data
        await message.reply(response)
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")


# Основная асинхронная функция
async def main():
    dp.include_router(router)  # Подключаем маршрутизатор к диспетчеру
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
