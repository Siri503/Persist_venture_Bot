import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Initialize the bot with your bot token
bot = telebot.TeleBot("7816975026:AAGU2PbBIfAAXyi1FOWEhvwwMTQA60gq7MY")

# Main menu keyboard
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.row(KeyboardButton("/newbot"), KeyboardButton("/mybots"))
    markup.row(KeyboardButton("/setname"), KeyboardButton("/setdescription"), KeyboardButton("/setabouttext"))
    markup.row(KeyboardButton("/setuserpic"), KeyboardButton("/setcommands"), KeyboardButton("/deletebot"))
    markup.row(KeyboardButton("/token"), KeyboardButton("/revoke"))
    markup.row(KeyboardButton("/setinline"), KeyboardButton("/setinlinegeo"), KeyboardButton("/setinlinefeedback"))
    markup.row(KeyboardButton("/setjoingroups"), KeyboardButton("/setprivacy"))
    markup.row(KeyboardButton("/myapps"), KeyboardButton("/newapp"), KeyboardButton("/listapps"))
    markup.row(KeyboardButton("/editapp"), KeyboardButton("/deleteapp"))
    markup.row(KeyboardButton("/mygames"), KeyboardButton("/newgame"), KeyboardButton("/listgames"))
    markup.row(KeyboardButton("/editgame"), KeyboardButton("/deletegame"))
    return markup

# Helper function to send BotFather instructions
def send_botfather_instructions(chat_id, action):
    bot.send_message(chat_id, f"To {action}, use BotFather and follow the instructions.", reply_markup=main_menu())

# Command handlers
@bot.message_handler(commands=['start'])
def handle_start(message):
    with open('welcome.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)  # Sending the local image
    
    bot.send_message(
        message.chat.id,
        "Welcome! I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual.\n\nHere are your options:",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(
        message.chat.id,
        "Available commands:\n/start - Start the bot\n/help - Get help\n/newbot - Create a new bot\n/mybots - Edit your bots\n... and many more! Check the menu.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['newbot'])
def handle_newbot(message):
    bot.send_message(
        message.chat.id,
        "To create a new bot, follow the BotFather guide: https://core.telegram.org/bots#botfather",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['mybots'])
def handle_mybots(message):
    bot.send_message(
        message.chat.id,
        "You can edit your bots through BotFather. Visit: https://core.telegram.org/bots",
        reply_markup=main_menu()
    )

# Edit Bots section commands
@bot.message_handler(commands=['setname'])
def handle_setname(message):
    send_botfather_instructions(message.chat.id, "change the bot's name")

@bot.message_handler(commands=['setdescription'])
def handle_setdescription(message):
    send_botfather_instructions(message.chat.id, "change the bot description")

@bot.message_handler(commands=['setabouttext'])
def handle_setabouttext(message):
    send_botfather_instructions(message.chat.id, "change the bot about info")

@bot.message_handler(commands=['setuserpic'])
def handle_setuserpic(message):
    send_botfather_instructions(message.chat.id, "change the bot profile photo")

@bot.message_handler(commands=['setcommands'])
def handle_setcommands(message):
    send_botfather_instructions(message.chat.id, "update the bot's commands")

@bot.message_handler(commands=['deletebot'])
def handle_deletebot(message):
    send_botfather_instructions(message.chat.id, "delete your bot")

# Bot Settings section commands
@bot.message_handler(commands=['token'])
def handle_token(message):
    send_botfather_instructions(message.chat.id, "generate an authorization token")

@bot.message_handler(commands=['revoke'])
def handle_revoke(message):
    send_botfather_instructions(message.chat.id, "revoke your bot's token")

@bot.message_handler(commands=['setinline'])
def handle_setinline(message):
    send_botfather_instructions(message.chat.id, "toggle inline mode")

@bot.message_handler(commands=['setinlinegeo'])
def handle_setinlinegeo(message):
    send_botfather_instructions(message.chat.id, "toggle inline location requests")

@bot.message_handler(commands=['setinlinefeedback'])
def handle_setinlinefeedback(message):
    send_botfather_instructions(message.chat.id, "change inline feedback settings")

@bot.message_handler(commands=['setjoingroups'])
def handle_setjoingroups(message):
    send_botfather_instructions(message.chat.id, "can your bot be added to groups?")

@bot.message_handler(commands=['setprivacy'])
def handle_setprivacy(message):
    send_botfather_instructions(message.chat.id, "toggle privacy mode in groups")

# Web Apps section commands
@bot.message_handler(commands=['myapps'])
def handle_myapps(message):
    bot.send_message(
        message.chat.id,
        "To manage your web apps, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['newapp'])
def handle_newapp(message):
    bot.send_message(
        message.chat.id,
        "To create a new web app, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['listapps'])
def handle_listapps(message):
    bot.send_message(
        message.chat.id,
        "To get a list of your web apps, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['editapp'])
def handle_editapp(message):
    bot.send_message(
        message.chat.id,
        "To edit an existing web app, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['deleteapp'])
def handle_deleteapp(message):
    bot.send_message(
        message.chat.id,
        "To delete an existing web app, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

# Games section commands
@bot.message_handler(commands=['mygames'])
def handle_mygames(message):
    bot.send_message(
        message.chat.id,
        "To manage your games, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['newgame'])
def handle_newgame(message):
    bot.send_message(
        message.chat.id,
        "To create a new game, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['listgames'])
def handle_listgames(message):
    bot.send_message(
        message.chat.id,
        "To get a list of your games, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['editgame'])
def handle_editgame(message):
    bot.send_message(
        message.chat.id,
        "To edit an existing game, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['deletegame'])
def handle_deletegame(message):
    bot.send_message(
        message.chat.id,
        "To delete an existing game, refer to the Telegram Bot API documentation.",
        reply_markup=main_menu()
    )

# Catch-all for unknown messages
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.send_message(
        message.chat.id,
        "I didn't understand that. Please use the menu or type /help for a list of commands.",
        reply_markup=main_menu()
    )

print("Bot is running...")
bot.polling()
