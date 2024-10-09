import whois
from sec import API_KEY, bot_username, mo, p, h
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


################################################ COMMAND(/) SECTION ################################################
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = '''Hi Bot Telegram MyOpecs sedia memberikan bantuan.

Anda boleh pilih option di bawah untuk direct ke link website myopecs atau link tutorial di youtube.'''
    keyboard = [
        [InlineKeyboardButton("About my MyOpecs", url=mo)],
        [InlineKeyboardButton("Learn about Programming", url=p)],
        [InlineKeyboardButton("Learn about Hacking", url=h)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Open a inline markup link
    await update.message.reply_text(message, reply_markup=reply_markup)

#### WHOIS FUNCTION ####
async def lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        id = context.args[0]
        try:
            whois_info = whois.whois(id)
            response = f"Whois info for {id}:\n\n{whois_info}"
        except Exception as e:
            response = f"Error fetching whois info: {str(e)}"
    else:
        response = "Please provide an IP or domain after /whois."
    
    await update.message.reply_text(response)
###################################################################################################################



################################################ RESPON SECTION ################################################
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'hi bro or sis'
    
    if 'meow' in processed:
        return 'woff'
    
    return 'try lagi'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # message_type: str = update.message.chat.type
    text: str = update.message.text

    # if message_type == 'group':
    #     if bot_username in text:
    #         new_text: str = text.replace(bot_username, '').strip()
    #         response: str = handle_response(new_text)
    #     else:
    #         return
    
    # else:
    response: str = handle_response(text)

    await update.message.reply_text(response)
###################################################################################################################


################################################ ERROR SECTION ################################################
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
###################################################################################################################



################################################ MAIN ################################################
if __name__ == '__main__':
    print('Bot start...')
    app = Application.builder().token(API_KEY).build()

    ## Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('lookup', lookup))

    ## Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    ## Error
    app.add_error_handler(error)

    ## Poll bot
    print('polling...')
    app.run_polling(poll_interval=2)
###################################################################################################################
