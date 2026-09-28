import os
import asyncio
from gtts import gTTS
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8948615784:AAE3-W-unSktT2L8xT7CHyPrLOd57fiBXt4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Namaste! Mujhe koi bhi text bhejo, main audio bana kar bhejunga.")

async def text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    status_msg = await update.message.reply_text("Audio generate ho rahi hai...")

    audio_file = f"voice_{update.message.id}.mp3"

    try:
        tts = gTTS(text=user_text, lang="hi")
        tts.save(audio_file)

        with open(audio_file, "rb") as audio:
            await update.message.reply_audio(audio=audio, title="ReadMate Audio")

    except Exception as e:
        await update.message.reply_text(f"Dikkat aayi: {e}")

    finally:
        await status_msg.delete()
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == '__main__':
    print("Bot chalu ho raha hai...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), text_to_speech))
    print("Bot live hai!")
    app.run_polling()
  
