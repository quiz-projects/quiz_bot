from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{update.effective_user.first_name} - Welcome to Quiz bot!')


updater = Updater('1514048549:AAEKmDPsPzDIw3K4CBIPxUqko2AzQ7gCyQA')

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()