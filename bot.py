# -*- coding: utf8 -*-

import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)

arr = ["Напевно ти знаєш якийсь секрет краси, інакше як пояснити твою сногсшибательность'", "Ти, та, про кого я думаю кожну секунду, хвилину, годину, добу!", "Ти немов казковий квітка, ніжна, красива. Ти просто чарівність. Тобою милуюся, тебе обожнюю. Кожна хвилина, проведена з тобою, для мене нагорода. Найкращі компліменти тобі, моя кохана. Я хочу бути завжди з тобою поряд, слухати твій дзвінкий голосок, милуватися твоєю ніжною посмішкою, насолоджуватися ніжними поцілунками. Нехай тебе закрутить моєї любові потік, хай збудуться всі твої мрії, нехай життя твоє буде солодким і казковою. Будь завжди хранима долею. Нехай моя любов буде оберегом для тебе.", "Навіть мухи до тебе клеяться!", "З тобою добре і приємно, з тобою радісно, а дивитися на твою красу – суцільне задоволення!'", "Мені подобається, що ти знаєш, чого хочеш досягти в житті. Ти цілеспрямована дівчина, яка планує і добивається свого.", "Я зовсім не хотів сказати, що ти краще за всіх. Насправді це інші гірше тебе.", "Ти просто зобов’язана сходити в редакцію Космополітен, а то я чув їм ні як не знайти модель для головної сторінки.", "Навіть сонна ти гарна, як ангел!", "Ось тебе поруч немає і від мене немов відрізали половину. Або більше. Чекаю – не дочекаюся, коли знову стану цілим.", "Твоєї зовнішності позаздрить будь-супер модель.", "Все б віддав, щоб бути таким красивим, як ти, незважаючи на те, що я чоловік!", "В твоїх очах відбивається весь нескінченний космос!", "Як багато дівчат хороших, але ти не просто гарна – ти прекрасна!", "Неймовірна, дивна, незвичайна, промениста, чарівна, елегантна, витончена, граціозна, сяюча, витончена, талановита, різнобічна, освічена, розумна, кмітлива, благородна, неповторна. Ти просто дивовижна жінка: то пылаешь, як яскравий вогник, то растворяешь в собі весь світ, як крапля води.", "Твоя щира посмішка дозволяє відкривати будь-які двері!", "Твоя хода змушує спотикатися навіть впевнених у собі чоловіків.", "Ти така витончена!", "Мені подобається, як ти одягаєшся. Ти вмієш вибирати одяг.", "Вибач за мовчання, просто я вражений твоєю красою!"]

@bot.message_handler(commands=['start'])
def welcome(message):
    
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("😊 Комплімент")
 
    markup.add(item1)
 
    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створенний для того, щоб ти могла получати компліменти, коли душа забажає)".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
            
n = 0

@bot.message_handler(content_types=['text']) 
def lalala(message):
    f'{arr}' 
    global n
    try: 
        cum = arr[n]                                 
        bot.send_message(message.chat.id, cum)
        n += 1
    except: 
        n = 0

bot.polling(none_stop=True)