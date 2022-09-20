import telebot
import random

from telebot import types

bot = telebot.TeleBot("1833552275:AAGBLO0t22lLufnPhjOSOQaVbq0zAOQ6bMQ")

@bot.message_handler(commands=['start'])
def welcome(message):

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Зробити замовлення")
	item2 = types.KeyboardButton("Про нас")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добрий день, {0.first_name}, Я - <b>{1.first_name}</b>, з моєю допомогою Ви будете щасливі бачити на своєму автомобілі нові колеса.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, 'Спочатку вкажіть марку автомобіля')
    elif message.text == 'Про нас':

		markup = types.InlineKeyboardMarkup(row_width=2)
		item1 = types.InlineKeyboardButton("Зробити замовлення", callback_data='order')
		item2 = types.InlineKeyboardButton("Зворотній зв'язок", callback_data='feedback')

		markup.add(item1, item2)

		bot.send_message(message.chat.id, 'Ми компанія...', reply_markup=markup)
	else:
		bot.send_message(message.chat.id, 'Я не можу зрозуміти Ваше замовлення. Напишіть його ще раз, будь ласка')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'order':
                bot.send_message(call.message.chat.id, 'Спочатку вкажіть марку та модуль автомобіля, обєм двигуна та розмір дисків')
            elif call.data == 'feedback':
                bot.send_message(call.message.chat.id, 'Для детальної інформації можете телефонувати в робочі дні з 9 до 18 за телефоном 0123456789 (Павло)')

            # remove inline  buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ми компанія...', reply_markup=None)


    except Exception as e:
        print(repr(e))

#RUN
bot.polling(none_stop=True)
