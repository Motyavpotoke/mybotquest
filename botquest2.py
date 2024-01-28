import json
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

Bot_Token = ""
bot = TeleBot(Bot_Token)

with open('locations2.json', encoding='utf-8') as file:
    locations = json.load(file)


@bot.message_handler(commands=['start'])
def start_message(message):
    start_menu = locations["locations"]["start_menu"]["description"]
    markup = ReplyKeyboardMarkup(row_width=1)
    actions = locations["locations"]["start_menu"]["actions"]
    markup.add(*actions)
    bot.send_message(message.chat.id, start_menu, reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Начать квест")
def start(message):
        welcome_text = locations["locations"]['start']['description']
        image_url = locations["locations"]['start']['image_url']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['start']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        bot.send_photo(message.chat.id, image_url)

@bot.message_handler(func=lambda message: message.text == "Команды бота")
def comand(message):
    bot.send_message(message.chat.id, 'Мои команды: /start')

@bot.message_handler(func=lambda message: message.text)
def message_handler(message):
    if message.text == 'Ударить пенальти':
        welcome_text = locations["locations"]['penalty_shot']['description']
        image_url = locations["locations"]['penalty_shot']['image_url']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['penalty_shot']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        bot.send_photo(message.chat.id, image_url)
    elif message.text == 'Сделать дальний удар':
        welcome_text = locations["locations"]['long_shot']['description']
        image_url = locations["locations"]['long_shot']['image_url']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['long_shot']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        bot.send_photo(message.chat.id, image_url)
    elif message.text == 'Остаться поиграть':
        welcome_text = locations["locations"]['start_play']['description']
        image_url = locations["locations"]['start_play']['image_url']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['start_play']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        bot.send_photo(message.chat.id, image_url)
    elif message.text == "Уйти домой":
        back =  locations["locations"]['back']['description']
        image_url = locations["locations"]['back']['image_url']
        bot.send_message(message.chat.id, back )
        bot.send_photo(message.chat.id, image_url)
        welcome_text = locations["locations"]['start_menu']['description']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['start_menu']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
    elif message.text == 'Пойти на футбольное поле':
        welcome_text = locations["locations"]['fotball']['description']
        image_url = locations["locations"]['fotball']['image_url']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['fotball']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        bot.send_photo(message.chat.id, image_url)
    elif message.text == 'Посетить баскетбольную площадку':
        welcome_text = locations["locations"]['basketball_court']['description']
        image_url = locations["locations"]['basketball_court']['image_url']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['basketball_court']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        bot.send_photo(message.chat.id, image_url)
    elif message.text == 'Посетить хоккейное поле':
        welcome_text = locations["locations"]['hockey_rink']['description']
        image_url = locations["locations"]['hockey_rink']['image_url']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['hockey_rink']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        bot.send_photo(message.chat.id, image_url)
    elif message.text == "Ударить в левый угол":
        miss =  locations["locations"]['miss']['description']
        image_url = locations["locations"]['miss']['image_url']
        bot.send_message(message.chat.id, miss )
        bot.send_photo(message.chat.id, image_url)
        welcome_text = locations["locations"]['start']['description']
        image_url = locations["locations"]['start']['image_url']
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]['start']["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
        bot.send_photo(message.chat.id, image_url)
    elif message.text == "Ударить в правый угол":
        goal =  locations["locations"]['goal']['description']
        image_url = locations["locations"]['goal']['image_url']
        bot.send_message(message.chat.id, goal )
        bot.send_photo(message.chat.id, image_url)
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)
    elif message.text == "Выполнить удар в верхний правый угол":
        da =  locations["locations"]['da']['description']
        image_url = locations["locations"]['da']['image_url']
        bot.send_message(message.chat.id, da )
        bot.send_photo(message.chat.id, image_url)
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)
    elif message.text == "Средний бросок":
        mid_range_shot = locations["locations"]['mid_range_shot']['description']
        image_url = locations["locations"]['mid_range_shot']['image_url']
        bot.send_message(message.chat.id, mid_range_shot)
        bot.send_photo(message.chat.id, image_url)
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)
    elif message.text == "Трёхочковый бросок":
        three_point_shot = locations["locations"]['three_point_shot']['description']
        image_url = locations["locations"]['three_point_shot']['image_url']
        bot.send_message(message.chat.id, three_point_shot)
        bot.send_photo(message.chat.id, image_url)
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)
    elif message.text == "Штрафной бросок":
        free_throw = locations["locations"]['free_throw']['description']
        image_url = locations["locations"]['free_throw']['image_url']
        bot.send_message(message.chat.id, free_throw)
        bot.send_photo(message.chat.id, image_url)
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)
    elif message.text == "Выполнить удар по центру":
        miss = locations["locations"]['miss']['description']
        image_url = locations["locations"]['miss']['image_url']
        bot.send_message(message.chat.id, miss)
        bot.send_photo(message.chat.id, image_url)
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)
    elif message.text == "Вернуться назад" :
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)
    elif message.text == "Выполнить буллит" :
        shoot = locations["locations"]['shoot']['description']
        image_url = locations["locations"]['shoot']['image_url']
        bot.send_message(message.chat.id, shoot)
        bot.send_photo(message.chat.id, image_url)
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)
    elif message.text == "Отдать возможность выполнить буллит своему товарищу" :
        team_shoot = locations["locations"]['team_shoot']['description']
        image_url = locations["locations"]['team_shoot']['image_url']
        bot.send_message(message.chat.id, team_shoot)
        bot.send_photo(message.chat.id, image_url)
        start_menu = locations["locations"]["start_menu"]["description"]
        markup = ReplyKeyboardMarkup(row_width=1)
        actions = locations["locations"]["start_menu"]["actions"]
        markup.add(*actions)
        bot.send_message(message.chat.id, start_menu, reply_markup=markup)




bot.polling()
