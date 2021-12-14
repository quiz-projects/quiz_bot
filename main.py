#Import libarary
from telegram import Update
from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    Filters,
    CallbackContext)

#Define start function
def start(update:Update, context:CallbackContext):
    """
    Send a message when the command /start is issued.
    """
    #Define message
    msg = "Hello World!"
    #Send message
    update.message.reply_text(msg)

#Define main function
def main():
    """
    Run the bot
    """
    #Define TOKEN
    TOKEN = '1602686596:AAECWOgNbMCkfTUAxYEtKJFtnej6H6Dp5TA'
    #Define updater
    updater = Updater(TOKEN)
    #Define dispatcher
    dp = updater.dispatcher
    #Define command handler for start
    dp.add_handler(CommandHandler("start", start))
    # Start the Bot
    updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

#Run main function
if __name__ == "__main__":
    main()