import requests
import datetime
from config import tg_bot_token, open_weather_token
from  aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot= Bot (tg_bot_token)
dp = Dispatcher (bot)


@dp.message_handler(commands=["start"])
async def start_command (message: types.Message):
    await message.reply("Привет, напиши мне название города и я пришлю сводку погоды!")

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно\U00002600",
        "Clouds": "Облачно\U00002601",
        "Rain": "Дождь\U00002614",
        "Trunderstorm": "Гроза\U000026A1",
        "Snow": "Снег\U0001F328",
        "Mist": "Туман\U0001F32B"

    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
n
        data = r.json()
        # pprint(data)git

        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри сам в окно'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        await message.reply(
            f'Погода в городе: {city}\nТемпература: {cur_weather}{wd}\nВлажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind}м/с\n "Хорошего дня!!!"')


    except:
        await message.reply('\U00002620 Проверьте название города\U00002620')


def main():
    city = input('Введите город:')
    get_weather(city, open_weather_token)

if __name__=='__main__':
    executor.start_polling(dp)