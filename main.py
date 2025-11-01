import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import re

# === Sozlamalar ===
BOT_TOKEN = "8114837659:AAHYY_MbvGE2J_ps7M98MmYVljBCNJavGVE"
ADMIN_ID = 6234736126
CARD_NUMBER = "9860 1678 2074 3752"
CARD_OWNER = "I. TORAXON"

bot = telebot.TeleBot(BOT_TOKEN)

# === Formatlash uchun ===
def format_amount(num):
    return f"{num:,}".replace(",", " ") + " so'm"


# === /start ===
@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⭐ Telegram Premium", callback_data="premium"))
    kb.add(InlineKeyboardButton("✨ Telegram Stars", callback_data="stars"))
    kb.add(InlineKeyboardButton("💎 Mobile Legends", callback_data="mlbb"))
    kb.add(InlineKeyboardButton("🎮 PUBG UC", callback_data="uc"))
    bot.send_message(message.chat.id, "👇 Quyidagi xizmatlardan birini tanlang:", reply_markup=kb)


# === Premium menyusi ===
def show_premium(chat_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("💎 12 Oylik — 410 000 so'm", callback_data="buy:premium:12 oylik:410000"))
    kb.add(InlineKeyboardButton("💎 6 Oylik — 245 000 so'm", callback_data="buy:premium:6 oylik:245000"))
    kb.add(InlineKeyboardButton("💎 3 Oylik — 170 000 so'm", callback_data="buy:premium:3 oylik:170000"))
    kb.add(InlineKeyboardButton("💎 1 Oylik — 50 000 so'm", callback_data="buy:premium:1 oylik:50000"))
    kb.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="back"))
    text = (
        "👑 <b>Telegram Premium</b>\n\n"
        "💫 Muddati bo‘yicha tanlang:\n"
        "💎 12 oylik — 410 000 so'm\n"
        "💎 6 oylik — 245 000 so'm\n"
        "💎 3 oylik — 170 000 so'm\n"
        "💎 1 oylik — 50 000 so'm"
    )
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=kb)


# === Stars menyusi ===
def show_stars(chat_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("⭐ 10000 — 2 400 000 so'm", callback_data="buy:stars:10000⭐:2400000"))
    kb.add(InlineKeyboardButton("⭐ 5000 — 1 200 000 so'm", callback_data="buy:stars:5000⭐:1200000"))
    kb.add(InlineKeyboardButton("⭐ 2500 — 600 000 so'm", callback_data="buy:stars:2500⭐:600000"))
    kb.add(InlineKeyboardButton("⭐ 1500 — 360 000 so'm", callback_data="buy:stars:1500⭐:360000"))
    kb.add(InlineKeyboardButton("⭐ 1000 — 240 000 so'm", callback_data="buy:stars:1000⭐:240000"))
    kb.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="back"))
    text = (
        "✨ <b>Telegram Stars</b>\n\n"
        "⭐ Tanlang:\n"
        "1000⭐ — 240 000 so'm\n"
        "1500⭐ — 360 000 so'm\n"
        "2500⭐ — 600 000 so'm\n"
        "5000⭐ — 1 200 000 so'm\n"
        "10000⭐ — 2 400 000 so'm"
    )
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=kb)


# === Mobile Legends menyusi ===
def show_mlbb(chat_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("💎 1000💎 — 260 000 so'm", callback_data="buy:mlbb:1000💎:260000"))
    kb.add(InlineKeyboardButton("💎 514💎 — 135 000 so'm", callback_data="buy:mlbb:514💎:135000"))
    kb.add(InlineKeyboardButton("💎 257💎 — 70 000 so'm", callback_data="buy:mlbb:257💎:70000"))
    kb.add(InlineKeyboardButton("💎 172💎 — 47 000 so'm", callback_data="buy:mlbb:172💎:47000"))
    kb.add(InlineKeyboardButton("💎 86💎 — 25 000 so'm", callback_data="buy:mlbb:86💎:25000"))
    kb.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="back"))
    text = (
        "💎 <b>Mobile Legends</b>\n\n"
        "💠 Tanlang:\n"
        "1000💎 — 260 000 so'm\n"
        "514💎 — 135 000 so'm\n"
        "257💎 — 70 000 so'm\n"
        "172💎 — 47 000 so'm\n"
        "86💎 — 25 000 so'm"
    )
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=kb)


# === PUBG UC menyusi ===
def show_uc(chat_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🎮 3850 UC — 590 000 so'm", callback_data="buy:uc:3850 UC:590000"))
    kb.add(InlineKeyboardButton("🎮 1800 UC — 300 000 so'm", callback_data="buy:uc:1800 UC:300000"))
    kb.add(InlineKeyboardButton("🎮 660 UC — 120 000 so'm", callback_data="buy:uc:660 UC:120000"))
    kb.add(InlineKeyboardButton("🎮 325 UC — 65 000 so'm", callback_data="buy:uc:325 UC:65000"))
    kb.add(InlineKeyboardButton("🎮 60 UC — 13 000 so'm", callback_data="buy:uc:60 UC:13000"))
    kb.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="back"))
    text = (
        "🎮 <b>PUBG Mobile UC</b>\n\n"
        "💠 Tanlang:\n"
        "3850 UC — 590 000 so'm\n"
        "1800 UC — 300 000 so'm\n"
        "660 UC — 120 000 so'm\n"
        "325 UC — 65 000 so'm\n"
        "60 UC — 13 000 so'm"
    )
    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=kb)


# === Callbacklar ===
@bot.callback_query_handler(func=lambda c: True)
def callbacks(call):
    data = call.data

    if data == "premium":
        show_premium(call.message.chat.id)
    elif data == "stars":
        show_stars(call.message.chat.id)
    elif data == "mlbb":
        show_mlbb(call.message.chat.id)
    elif data == "uc":
        show_uc(call.message.chat.id)
    elif data == "back":
        start(call.message)

    elif data.startswith("buy:"):
        _, service, tariff, price = data.split(":")
        send_payment_info(call.message.chat.id, service, tariff, int(price))


# === To‘lov ma’lumotlari ===
def send_payment_info(chat_id, service, tariff, price):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("✅ Men to‘lov qildim", callback_data=f"paid:{service}:{tariff}:{price}"))
    kb.add(InlineKeyboardButton("⬅️ Orqaga", callback_data=service))

    text = (
        f"💳 <b>To‘lov ma’lumotlari</b>\n\n"
        f"🔹 Xizmat: {service.upper()}\n"
        f"📦 Paket: {tariff}\n"
        f"💰 Narx: <b>{format_amount(price)}</b>\n\n"
        f"💳 Karta raqami: <code>{CARD_NUMBER}</code>\n"
        f"Karta egasi: {CARD_OWNER}\n\n"
        f"✅ To‘lov qilgach, pastdagi tugmani bosing."
    )

    bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=kb)


# === To‘lovdan so‘ng ===
@bot.callback_query_handler(func=lambda c: c.data.startswith("paid:"))
def handle_paid(call):
    _, service, tariff, price = call.data.split(":")
    msg = bot.send_message(call.message.chat.id, "💳 To‘lov qildingizmi? Karta oxirgi 4 raqamini yuboring:")
    bot.register_next_step_handler(msg, process_card_last4, service, tariff, price)


def process_card_last4(message, service, tariff, price):
    if not re.fullmatch(r"\d{4}", message.text.strip()):
        msg = bot.send_message(message.chat.id, "❌ Faqat 4 ta raqam kiriting!")
        bot.register_next_step_handler(msg, process_card_last4, service, tariff, price)
        return
    msg = bot.send_message(message.chat.id, "Ism va familiyangizni yuboring:")
    bot.register_next_step_handler(msg, process_fullname, message.text.strip(), service, tariff, price)


def process_fullname(message, card4, service, tariff, price):
    fullname = message.text.strip()
    formatted = format_amount(int(price))

    bot.send_message(message.chat.id, f"✅ Ma'lumot yuborildi. Admin tez orada tasdiqlaydi.")
    admin_text = (
        f"📩 <b>Yangi to‘lov</b>\n\n"
        f"🔹 Xizmat: {service.upper()}\n"
        f"📦 Paket: {tariff}\n"
        f"💰 Narx: {formatted}\n\n"
        f"👤 Foydalanuvchi: @{message.from_user.username or '—'} (id: {message.from_user.id})\n"
        f"👨‍💼 Ism Familiya: {fullname}\n"
        f"💳 Karta (oxirgi 4): ****{card4}"
    )
    bot.send_message(ADMIN_ID, admin_text, parse_mode="HTML")


# === Botni ishga tushirish ===
print("🤖 Bot ishga tushdi...")
bot.infinity_polling(skip_pending=True)
