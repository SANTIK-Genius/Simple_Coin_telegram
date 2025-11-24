import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

TOKEN = "YOUR_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Подкинуть"))

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Привет! Жми кнопку!", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
	if message.text == "Подкинуть":
		result = random.choice(["Да", "Потом"])
		bot.send_message(message.chat.id, f"Ответ: {result}")
	else:
		bot.send_message(message.chat.id, "Нажми на кнопку 😉")

bot.polling()

