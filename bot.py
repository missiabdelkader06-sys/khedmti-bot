from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.environ.get("TOKEN", "8736731932:AAGgXq3wO_S4M5SHtRfzk__u4IMewuVPAdQ")

def start(update, context):
    update.message.reply_text("ahlan! ana Khedmti Bot")

def handle_message(update, context):
    update.message.reply_text(update.message.text)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
updater.idle()
