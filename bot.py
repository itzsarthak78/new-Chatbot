import os
import telebot
import google.generativeai as genai

# 1. Setup API Keys (Environment Variables se uthayega)
BOT_TOKEN = os.environ.get('TELEGRAM_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

# 2. Configure Gemini
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Your name is Sarthak. You are a funny, sarcastic Indian boy. Reply in Hinglish. Use slang like 'Bhai', 'Scene', 'Gazab'. Roast the user lightly if they ask boring stuff."
)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def chat_with_sarthak(message):
    try:
        # Chat history ke bina simple reply
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(e)
        bot.reply_to(message, "Arre bhai, server phat gaya lagta hai. Dobara try kar!")

print("Sarthak is online...")
bot.infinity_polling()
