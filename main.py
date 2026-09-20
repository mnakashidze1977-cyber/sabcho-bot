import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
print(f"TOKEN exists: {bool(TOKEN)}")

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "sabcho-bot is live!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("გამარჯობა! ბოტი მუშაობს ✅\nდამიწერე კითხვა.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.message.text
    await update.message.reply_text(f"შენი კითხვა: {q}\n\nმალე AI პასუხიც დაემატება!")

def run_bot():
    if not TOKEN:
        print("ERROR: BOT_TOKEN not found in Environment!")
        return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("Bot polling started...")
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
