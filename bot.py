import os
import telebot
from google import genai

bot = telebot.TeleBot(os.environ["TELEGRAM_BOT_TOKEN"])
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.infinity_polling()