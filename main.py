import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

START_MESSAGE = """
🛸 *Welcome to Drone-CDS*

Drone-CDS is an automated computer-vision monitoring system designed for real-time road inspection. It detects potholes, filters out false positives like road paint and tar patches, and broadcasts live alert notifications.

🔗 *GitHub Repository:*
https://github.com/reyanshgugnani23/Drone-CDS

🛠️ *Quick Setup Steps:*

1️⃣ `git clone https://github.com/reyanshgugnani23/Drone-CDS.git`

2️⃣ `cd Drone-CDS`

3️⃣ `pip install -r requirements.txt`

4️⃣ Add your `.env` file with `TELEGRAM_BOT_TOKEN`

5️⃣ Run `python main.py`
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        START_MESSAGE,
        parse_mode="Markdown"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🛸 Drone-CDS bot started")
    app.run_polling()


if __name__ == "__main__":
    main()
