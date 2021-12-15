from telegram import Update, ReplyKeyboardMarkup, ReplyMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Document, PhotoSize
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, PollAnswerHandler, PollHandler, CallbackQueryHandler
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
    # Create a button from the list of quizzes
    buttons = [[InlineKeyboardButton(button,callback_data=button)] for button in all_quiz]
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(text='Choose the one you need from the Quiz below',reply_markup=reply_markup)

def choose_quiz(update,context):
    bot = context.bot
    query = update.callback_query
    callback_data = query.data
    questions = db.get_quiz(callback_data)
    chat_id = update.callback_query.message.chat.id
    for i,quiz in enumerate(questions):
        question = quiz['question']
        image_link = quiz['image_link']
        options = [str(option) for option in quiz['options']]
        correct_answer = quiz['correct']
        correct_id = 0

        for i,option in enumerate(options):
            if correct_answer == option:
                correct_id = i

        if i == 0:
            query.edit_message_text(text=start)
            bot.sendPhoto(chat_id,image_link,caption='#python #test #print')
            bot.send_poll(chat_id, question,options,is_anonymous=False,type='quiz',correct_option_id=correct_id,open_period=5)
        else:
            bot.sendPhoto(chat_id,image_link,caption='#python #test #print')
            bot.send_poll(chat_id, question,options,is_anonymous=False,type='quiz',correct_option_id=correct_id,open_period=5)


updater = Updater('1514048549:AAEKmDPsPzDIw3K4CBIPxUqko2AzQ7gCyQA')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('quiz', quiz))
updater.dispatcher.add_handler(MessageHandler(Filters.document,document))
updater.dispatcher.add_handler(CallbackQueryHandler(choose_quiz))

updater.start_polling()
updater.idle()