from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Obtenemos el token de las variables de entorno
TOKEN = os.getenv("TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 ¡Hola! Soy el bot oficial de Códigos Jeferplay.\nUsa /help para ver los comandos disponibles."
    )

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧩 COMANDOS DISPONIBLES:\n"
        "/start - Inicia el bot\n"
        "/help - Muestra este menú de ayuda\n"
        "/info - Muestra tu información\n"
        "/about - Acerca del bot"
    )

# Comando /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"ℹ️ INFO\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}\n"
        f"😎 CLIENTE: True"
    )

# Comando /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 Bot desarrollado por Jeferplay 🎮\n¡Gracias por usarme!"
    )

# Configuración principal del bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("about", about))

print("✅ BOT DE CÓDIGOS JEFERPLAY INICIADO...")
app.run_polling()
