from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = "8610528069:AAH3H-ryTzTfRkx880lDTSt6sSFk5gz_Fg4"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🎮 Играть",
                web_app=WebAppInfo(
                    url="https://example.com"
                )
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎁 Добро пожаловать в Case Game!\n\nНажми кнопку и начни игру:",
        reply_markup=reply_markup
    )


app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler("start", start)
)


print("Бот работает!")

app.run_polling()
