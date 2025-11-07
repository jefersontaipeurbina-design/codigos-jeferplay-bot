from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import json

TOKEN = os.getenv("TOKEN")

# =============================
# CLIENTES REGISTRADOS MANUALMENTE
# =============================
clientes = {
    "8342506652": {
        "username": "Je Fer Play",
        "first_name": "Je Fer Play",
        "is_client": True
    }
}

# Archivo donde se guardarán los clientes nuevos
CLIENTES_FILE = "clientes.json"

# Cargar los clientes guardados en archivo (si existe)
if os.path.exists(CLIENTES_FILE):
    with open(CLIENTES_FILE, "r") as f:
        guardados = json.load(f)
        clientes.update(guardados)

# =============================
# COMANDOS DEL BOT
# =============================

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = str(user.id)

    if user_id not in clientes:
        clientes[user_id] = {
            "username": user.username,
            "first_name": user.first_name,
            "is_client": True
        }
        with open(CLIENTES_FILE, "w") as f:
            json.dump(clientes, f, indent=4)
        await update.message.reply_text(f"👋 ¡Hola {user.first_name}! Te he registrado como cliente ✅")
    else:
        await update.message.reply_text(f"👋 ¡Hola {user.first_name}! Ya eres cliente 😎")

# /clientes
async def ver_clientes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(clientes) == 0:
        await update.message.reply_text("📭 No hay clientes registrados todavía.")
    else:
        lista = "\n".join(
            [f"👤 {info['first_name']} (@{info['username']}) - ID: {uid}" for uid, info in clientes.items()]
        )
        await update.message.reply_text(f"📋 Lista de clientes registrados:\n\n{lista}")

# /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = str(user.id)
    es_cliente = "Sí ✅" if user_id in clientes else "No ❌"
    await update.message.reply_text(
        f"ℹ️ INFO\nUsername: {user.first_name}\nID: {user.id}\n😎 CLIENTE: {es_cliente}"
    )

# =============================
# CONFIGURACIÓN DEL BOT
# =============================
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("clientes", ver_clientes))
app.add_handler(CommandHandler("info", info))

print("✅ BOT DE CÓDIGOS JEFERPLAY INICIADO...")
app.run_polling()
