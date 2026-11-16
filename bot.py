import os

from telegram import Update

from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["TELEGRAM_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "🚗 KELEPİR ARAÇ RADARI AKTİF!\n\n"

        "Takip kriterleri:\n"

        "• Tüm binek otomobiller\n"

        "• 200.000 - 800.000 TL\n"

        "• Piyasanın en az %25 altı\n\n"

        "Bildirim sistemi hazırlanıyor."

    )

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "✅ Telegram bağlantısı çalışıyor!"

    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("test", test))

app.run_polling()
