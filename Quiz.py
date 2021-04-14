import logging
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,Update
from telegram.ext import Updater,CommandHandler,CallbackQueryHandler,CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

correct_answers = 0

question2 = {'Нидерланды': 1,
             'Россия': 0,
             'Франция': 0,
             'Монако': 0
             }

question3 = {'Нью-Йорк': 0,
             'Вашингтон': 1,
             'Лос-Анджелес': 0,
             'Майами': 0
             }


def start(update: Update, _: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("4", callback_data='0'),
            InlineKeyboardButton("5", callback_data='0'),
        ],
        [
            InlineKeyboardButton("6", callback_data='1'),
            InlineKeyboardButton("7", callback_data='0'),
        ],
    ]
    update.message.reply_text('🌍 Сколько материков на планете Земля?', reply_markup=InlineKeyboardMarkup(keyboard))

def button(update: Update, _: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    global correct_answers
    correct_answers += int(query.data)
    update.callback_query.message.edit_text(f'Правильных ответов: {correct_answers}.')

def help_command(update: Update,_: CallbackContext) -> None:
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    updater = Updater("TOKEN")  # TOKEN
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
