import os
from flask import Flask
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "გამარჯობა! მე ვარ შენი საბჭოს AI.\n"
        "დამისვი კითხვა საბჭოს შესახებ და გასცემ პასუხს.\n"
        "რიგდება 5 ვარიანტს ერთად."
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.message.text
    await update.message.reply_text(f"შეკითხვა: {q}\n\nსამწუხაროდ პასუხის მოდული ჯერ კავშირზეა Vertex-თან.")

def run():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run).start()
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
