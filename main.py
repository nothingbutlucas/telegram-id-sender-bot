#!/usr/bin/env python
import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

"""Este bot te envia tu id de telegram junto con el id de la conversación"""

TOKEN = os.environ.get("TOKEN")
HOLA_MSGS = ["hola", "hi", "hello", "que onda", "aloja"]

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
log = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    group_id = update.effective_message.chat_id
    await update.message.reply_html(
        f"Hola @{user.username}.\nEste es tu id: <code>{user.id}</code>\nEste es el id de este chat: <code>{group_id}</code>\n",
    )


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("source_code", handle_ver_codigo))
    application.add_handler(CommandHandler("support", handle_donaciones))
    application.run_polling()


def handle_donaciones(update, context):
    user_first_name = update.effective_user["first_name"]
    user_language = update.effective_user["language_code"]
    if user_language == "es":
        mensaje = (
            f"{user_first_name}! Si el bot te fue de utilidad y te ahorro tiempo, considera hacerme una donación."
            f"Me vendría bien para mantener el server y pagar la luz."
            f"\nPodes hacerlo desde ko-fi (botón aquí abajo)"
        )
        button = f"Comprame un Ko-Fi ☕"
    else:
        mensaje = (
            f"{user_first_name}! If the bot was useful and saved you time, consider making a donation to me."
            f"It will be a good idea to keep the server and keep the lights on."
            f"\nYou can do it from ko-fi (button below)"
        )
        button = f"Buy me a Ko-Fi ☕"

    update.message.reply_text(
        text=mensaje,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=button, url="https://ko-fi.com/nothingbutlucas"
                    )
                ],
            ]
        ),
    )


def handle_message(update, context):
    user_first_name = update.effective_user["first_name"]
    user_language = update.effective_user["language_code"]
    text = update.message.text.lower().strip()
    if text in HOLA_MSGS:
        if user_language == "es":
            hola_response = f"Hola {user_first_name}!"
        else:
            hola_response = f"Hi {user_first_name}!"

        update.message.reply_text(text=hola_response, parse_mode="html")


def handle_ver_codigo(update, context):
    user_first_name = update.effective_user["first_name"]
    user_language = update.effective_user["language_code"]
    if user_language == "es":
        response = (
            f"Hola {user_first_name}! Puedes ver el codigo en GitHub usando el botón de abajo!"
            f"<i>De paso seguime ;)</i>"
        )
        button = f"Ver el codigo en GitHub"
    else:
        response = (
            f"Hi {user_first_name}! You can see the code on GitHub using the button below!"
            f"\n<i>By the way, follow me!</i>"
        )
        button = f"See the code on GitHub"

    update.message.reply_text(
        text=response,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=button,
                        url="https://github.com/nothingbutlucas/telegram-id-sender-bot",
                    )
                ],
            ]
        ),
    )


while __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log.error(e)
