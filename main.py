from telegram import Update, ReplyKeyboardMarkup, ReplyMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Document, PhotoSize
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, PollAnswerHandler, PollHandler
import db
import os
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{update.effective_user.first_name} - Welcome to Quiz bot!')

def document(update,context):
    bot = context.bot
    document = update.message.document
    doc = context.bot.get_file(document).download()
    data_quiz = db.read_data_csv(doc)
    db.add_quiz(data_quiz,document.file_name[:-4])
    os.system(f"rm -r {doc}")

def quiz(update,context):
    all_quiz = db.read_quiz_data()
    buttons = [[InlineKeyboardButton(button,callback_data=button)] for button in all_quiz]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(text='Choose the one you need from the Quiz below',reply_markup=reply_markup)



updater = Updater('1514048549:AAEKmDPsPzDIw3K4CBIPxUqko2AzQ7gCyQA')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('quiz', quiz))
updater.dispatcher.add_handler(MessageHandler(Filters.document,document))


updater.start_polling()
updater.idle()