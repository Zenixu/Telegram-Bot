from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "7764455626:AAFpHYnRwfIm1Ic5jFqSPhu57ZqPGBgWwD0"
BOT_USERNAME: Final = "@Writerzie_bot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Haii!! Makasii yaa udah chat aku")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("baik ada yang bisa saya bantu?")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("kamu bisa menggunakan sebuah custom chat")


def handle_response(text: str) -> str:
    processed: str =text.lower()

    if "hai" in processed:
        return "haii jugaa"

    if "aku memiliki sebuah pertanyaan" in processed:
        return "apakah itu?"

    if "bagaimana pendapatmu tentang python?" in processed:
        return "menurut saya python sangat menyenangkan"

    return "aku belum mengerti yang kamu ketik...."



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return 
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    print("Memulai Bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Polling....")
    app.run_polling(poll_interval=3)