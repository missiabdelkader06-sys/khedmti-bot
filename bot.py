from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
TOKEN = os.environ.get("TOKEN", "8736731932:AAGgXq3wO_S4M5SHtRfzk__u4IMewuVPAdQ")
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")
    def log_message(self, format, *args):
        pass
def run_server():
    server = HTTPServer(("0.0.0.0", int(os.environ.get("PORT", 8080))), Handler)
    server.serve_forever()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ahlan! ana Khedmti Bot")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(text)
threading.Thread(target=run_server, daemon=True).start()
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print("bot running")
app.run_polling()
