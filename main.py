# -*- coding: utf-8 -*-
# Telegram-бот Натальи Орлова: услуги, запись, частые вопросы, контакты.
# Все тексты и ссылки лежат в самом верху файла — их легко менять.

import os
import sys

import telebot
from telebot import types

# ============================================================
# 1. НАСТРОЙКИ — здесь нужно вставить два значения
# ============================================================

# Токен — длинный «пароль» бота, который выдаёт BotFather.
# Вставьте его между кавычками вместо текста.
TOKEN = os.getenv("BOT_TOKEN", "ВСТАВЬТЕ_СЮДА_ТОКЕН_ОТ_BOTFATHER")

# Ваш личный номер (ID) в Telegram — куда бот будет присылать заявки.
# Как его узнать, написано в инструкции. Пока не знаете — оставьте 0.
OWNER_ID = int(os.getenv("OWNER_ID", "6243442767"))

# ============================================================
# 2. ССЫЛКИ
# ============================================================

LINK_TELEGRAM = "https://t.me/Natalika979"
LINK_VK = "https://vk.ru/natalka1979"
LINK_MAX = "https://go-save.ru/WA2hF"

# ============================================================
# 3. ТЕКСТЫ (можно менять)
# ============================================================

WELCOME = (
    "Здравствуйте! 👋\n"
    "Я помощник Натальи Орловой. Наталья создаёт сайты-визитки, лендинги, "
    "квизы и Telegram-ботов с помощью нейросети Claude.\n\n"
    "Первая структура вашего сайта — бесплатно.\n\n"
    "Выберите, что вас интересует, кнопками внизу 👇"
)

SERVICES_TEXT = (
    "💼 Услуги и цены\n\n"
    "▫️ Сайт-визитка — от 5 000 ₽\n"
    "Коротко о вас, ваши услуги и цены, контакты и кнопка связи. "
    "Самый популярный вариант для небольшого дела.\n\n"
    "▫️ Лендинг — от 10 000 ₽\n"
    "Одностраничный сайт под одну цель: продать услугу или собрать заявки.\n\n"
    "▫️ Квиз — от 8 000 ₽\n"
    "Короткий тест из нескольких вопросов. В конце человек оставляет свой контакт.\n\n"
    "▫️ Telegram-бот — от 10 000 ₽\n"
    "Программа в мессенджере, которая отвечает клиентам и выполняет действия.\n\n"
    "Чтобы оставить заявку, нажмите «📝 Запись»."
)

# Частые вопросы: (вопрос, ответ). Можно добавлять новые строки по образцу.
FAQ = [
    (
        "Сколько делается работа?",
        "Обычно работа занимает 3–7 дней.",
    ),
    (
        "Как проходит оплата?",
        "Мы подписываем простой договор. Предоплата 50% — до начала работы, "
        "оставшиеся 50% — когда вы принимаете готовую работу.",
    ),
    (
        "Что значит «бесплатная структура»?",
        "Вы рассказываете о своём деле, а Наталья показывает, из каких блоков "
        "будет состоять ваш сайт и что на нём стоит разместить. Это бесплатно.",
    ),
    (
        "Для кого вы работаете?",
        "Для небольшого бизнеса, самозанятых и разных мастеров.",
    ),
    (
        "Как проходит работа?",
        "Шесть простых шагов:\n"
        "1. Знакомство — вы рассказываете о задаче, мы ставим цель и сроки.\n"
        "2. Черновик — показываю структуру сайта.\n"
        "3. Договор и предоплата 50%.\n"
        "4. Создание сайта — обычно 3–7 дней.\n"
        "5. Проверка и правки — вносим правки до нужного вида.\n"
        "6. Сдача — вы принимаете работу и оплачиваете оставшиеся 50%.",
    ),
]

CONTACT_TEXT = "📞 Связаться с Натальей можно удобным для вас способом 👇"

THANKS_TEXT = "Спасибо! 🙌 Заявка принята, Наталья свяжется с вами."

# Названия кнопок главного меню
BTN_SERVICES = "💼 Услуги и цены"
BTN_ORDER = "📝 Запись"
BTN_FAQ = "❓ Частые вопросы"
BTN_CONTACT = "📞 Связаться со мной"
MENU_BUTTONS = [BTN_SERVICES, BTN_ORDER, BTN_FAQ, BTN_CONTACT]

# Варианты услуг в записи
SERVICE_CHOICES = [
    "Сайт-визитка",
    "Лендинг",
    "Квиз",
    "Telegram-бот",
    "Не знаю, нужна консультация",
]

# ============================================================
# 4. ЗАПУСК БОТА (ниже можно ничего не менять)
# ============================================================

if TOKEN.startswith("ВСТАВЬТЕ"):
    print("Ошибка: вставьте токен от BotFather в строку TOKEN в начале файла.")
    sys.exit(1)

bot = telebot.TeleBot(TOKEN)


def main_menu():
    """Кнопки меню под полем ввода."""
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(BTN_SERVICES, BTN_ORDER, BTN_FAQ, BTN_CONTACT)
    return kb


def contact_buttons():
    """Кнопки-ссылки: Telegram, VK, Max."""
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("Написать в Telegram", url=LINK_TELEGRAM),
        types.InlineKeyboardButton("Написать в VK", url=LINK_VK),
        types.InlineKeyboardButton("Написать в Max", url=LINK_MAX),
    )
    return kb


# ---------- Приветствие и служебные команды ----------

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, WELCOME, reply_markup=main_menu())


@bot.message_handler(commands=["myid"])
def my_id(message):
    # Нужна один раз, чтобы узнать свой ID для настройки OWNER_ID
    bot.send_message(message.chat.id, "Ваш ID: " + str(message.chat.id))


# ---------- Услуги и цены ----------

@bot.message_handler(func=lambda m: m.text == BTN_SERVICES)
def show_services(message):
    bot.send_message(message.chat.id, SERVICES_TEXT, reply_markup=main_menu())


# ---------- Частые вопросы ----------

@bot.message_handler(func=lambda m: m.text == BTN_FAQ)
def show_faq(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    for number, (question, _answer) in enumerate(FAQ):
        kb.add(types.InlineKeyboardButton(question, callback_data="faq_" + str(number)))
    bot.send_message(message.chat.id, "❓ Выберите вопрос:", reply_markup=kb)


@bot.callback_query_handler(func=lambda c: c.data.startswith("faq_"))
def show_faq_answer(call):
    bot.answer_callback_query(call.id)
    number = int(call.data.split("_")[1])
    question, answer = FAQ[number]
    bot.send_message(call.message.chat.id, question + "\n\n" + answer)


# ---------- Связаться со мной ----------

@bot.message_handler(func=lambda m: m.text == BTN_CONTACT)
def show_contacts(message):
    bot.send_message(message.chat.id, CONTACT_TEXT, reply_markup=contact_buttons())


# ---------- Запись (бот задаёт 4 вопроса по очереди) ----------

def route(message):
    """Если человек посреди записи нажал кнопку меню — переходим туда."""
    text = message.text or ""
    if text.startswith("/start"):
        start(message)
    elif text == BTN_SERVICES:
        show_services(message)
    elif text == BTN_ORDER:
        start_order(message)
    elif text == BTN_FAQ:
        show_faq(message)
    elif text == BTN_CONTACT:
        show_contacts(message)
    else:
        bot.send_message(message.chat.id, WELCOME, reply_markup=main_menu())


def left_form(message):
    """Проверка: не ушёл ли человек из записи. Если ушёл — возвращает True."""
    text = message.text
    if text is None:
        bot.send_message(
            message.chat.id,
            "Запись остановлена: мне нужен текст. Нажмите «📝 Запись», чтобы начать заново.",
            reply_markup=main_menu(),
        )
        return True
    if text.startswith("/") or text in MENU_BUTTONS:
        route(message)
        return True
    return False


@bot.message_handler(func=lambda m: m.text == BTN_ORDER)
def start_order(message):
    sent = bot.send_message(
        message.chat.id,
        "📝 Оставим заявку. Первая структура сайта — бесплатно.\n\nКак вас зовут?",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    bot.register_next_step_handler(sent, got_name, {})


def got_name(message, data):
    if left_form(message):
        return
    data["name"] = message.text.strip()
    sent = bot.send_message(message.chat.id, "Оставьте телефон или ник в Telegram для связи:")
    bot.register_next_step_handler(sent, got_contact, data)


def got_contact(message, data):
    if left_form(message):
        return
    data["contact"] = message.text.strip()
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for choice in SERVICE_CHOICES:
        kb.add(choice)
    sent = bot.send_message(message.chat.id, "Какая услуга вам нужна?", reply_markup=kb)
    bot.register_next_step_handler(sent, got_service, data)


def got_service(message, data):
    if left_form(message):
        return
    data["service"] = message.text.strip()
    sent = bot.send_message(
        message.chat.id,
        "Коротко о задаче: чем занимаетесь и что хотите получить?",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    bot.register_next_step_handler(sent, got_task, data)


def got_task(message, data):
    if left_form(message):
        return
    data["task"] = message.text.strip()

    send_to_owner(message, data)

    bot.send_message(message.chat.id, THANKS_TEXT, reply_markup=main_menu())
    bot.send_message(
        message.chat.id,
        "Если удобно, можно сразу написать Наталье напрямую 👇",
        reply_markup=contact_buttons(),
    )


def send_to_owner(message, data):
    """Отправляет заявку вам в личные сообщения."""
    user = message.from_user
    username = "@" + user.username if user.username else "ник не указан"
    text = (
        "🔔 Новая заявка из бота!\n\n"
        "Имя: " + data["name"] + "\n"
        "Контакт: " + data["contact"] + "\n"
        "Услуга: " + data["service"] + "\n"
        "Задача: " + data["task"] + "\n\n"
        "Telegram клиента: " + username + " (ID " + str(user.id) + ")"
    )
    if OWNER_ID == 0:
        print("ВНИМАНИЕ: OWNER_ID не заполнен, заявка никуда не отправлена:")
        print(text)
        return
    try:
        bot.send_message(OWNER_ID, text)
    except Exception as error:
        print("Не получилось отправить заявку владельцу:", error)


# ---------- Любой другой текст ----------

@bot.message_handler(func=lambda m: True)
def anything_else(message):
    bot.send_message(message.chat.id, "Выберите, пожалуйста, кнопку в меню 👇", reply_markup=main_menu())


print("Бот запущен. Чтобы остановить, нажмите Ctrl+C.")
bot.infinity_polling()
