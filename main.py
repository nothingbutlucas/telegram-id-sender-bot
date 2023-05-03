#!/usr/bin/env python
import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

"""Este bot te envia tu id de telegram junto con el id de la conversación"""

TOKEN = os.environ.get("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    group_id = update.effective_message.chat_id
    await update.message.reply_html(f"Hola @{user.username}.\nEste es tu id: <code>{user.id}</code>\nEste es el id de este chat: <code>{group_id}</code>\n",)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
