import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import json
from utils.util_heart import heart_main
from utils.util_sleep import sleep_main

with open("actions.json", "r") as f:
    actions = json.load(f)


def start(update, context):
    buttons = []

    for action in actions:
        button = InlineKeyboardButton(action, callback_data=action)
        buttons.append([button])

    keyboard = InlineKeyboardMarkup(buttons)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Select an action", reply_markup=keyboard)


def button(update, context):
    action = update.callback_query.data
    output = images = None

    if action == "Heart rate":
        output, images = heart_main(), ['./images/heart.png']
    elif action == "Sleep time":
        output = sleep_main(), ['./images/sleep.png']

    for out in output:
        context.bot.send_message(chat_id=update.effective_chat.id, text=out, parse_mode=telegram.ParseMode.HTML)
    for img in images:
        context.bot.send_document(chat_id=update.effective_chat.id, document=open(img, 'rb'))

    updater.dispatcher.add_handler(start_handler)
    

if __name__ == "__main__":
    updater = Updater("5580256888:AAG0KAM7ynNL9S7MnS_ZamPqrZ-k-xiCP0k", use_context=True)

    start_handler = CommandHandler("start", start)
    button_handler = CallbackQueryHandler(button)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(button_handler)

    updater.start_polling()
