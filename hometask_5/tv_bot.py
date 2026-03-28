import sqlite3
import requests
import telebot
from bs4 import BeautifulSoup
from telebot import types

BOT_TOKEN = "8587775599:AAEn4roW08AxYoyEludhnTh4uzqXf_C3wwU"

bot = telebot.TeleBot(BOT_TOKEN)
print("Бот стартанул")


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text="Конечно")
    button2 = types.KeyboardButton(text="Не сейчас")
    markup.add(button1, button2)
    bot.send_message(
        chat_id,
        f"Здравствуйте, {first_name}!\n"
        "Интересуетесь ассортиментом телевизоров SAMSUNG в магазине Электросила?",
        reply_markup=markup,
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    '''
    Какие нашёл баги:
    1. В цикле по page было +1, надо +2 т.к. второй элемент в рендже невключителен
    2. page_url логика с else и пустым page - избычточна
    '''
    chat_id = message.chat.id
    if message.chat.type == "private":
        if message.text == "Конечно":
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()

            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS products
                           (
                               id
                               INTEGER
                               PRIMARY
                               KEY
                               AUTOINCREMENT,
                               name
                               TEXT,
                               price_discounted
                               TEXT
                           )
                           ''')
            connection.commit()

            base_url = "https://sila.by/catalog/televizory/SAMSUNG"
            response = requests.get(base_url).text
            soup = BeautifulSoup(response, "html.parser")

            pagination = soup.find("div", class_="pages")
            if pagination:
                '''
                в общем кол-ве страниц -2 т.к. в pages a также используется для "показать ещё" и "Следующая"
                '''
                page_links = pagination.find_all("a")
                total_pages = len(page_links) - 2
            else:
                total_pages = 1

            for page in range(1, total_pages + 2):
                page_url = base_url + ("/page/" + str(page))
                response = requests.get(page_url).text
                soup = BeautifulSoup(response, "html.parser")
                sections = soup.find_all("div", class_="tovars")

                for section in sections:
                    products = section.find_all("div", class_="tov_prew")

                    for item in products:
                        product_name = item.find("strong").get_text(strip=True)
                        product_image = item.find("a").find("img").get("src")
                        product_link = item.find("a").get("href")

                        price_block = item.find("div", class_="price")
                        old_price_tag = price_block.find("s")
                        all_b = price_block.find_all("b")

                        if old_price_tag:
                            new_rub = all_b[0].get_text(strip=True)
                            new_kop = all_b[1].get_text(strip=True)
                            product_price_new = f"{new_rub}.{new_kop}"

                            old_b = old_price_tag.find_all("b")
                            old_rub = old_b[0].get_text(strip=True)
                            old_kop = old_b[1].get_text(strip=True)
                            product_price_old = f"{old_rub}.{old_kop}"
                        else:
                            rub = all_b[0].get_text(strip=True)
                            kop = all_b[1].get_text(strip=True)
                            product_price_new = f"{rub}.{kop}"
                            product_price_old = "Нет скидки"

                        product_screen_info_block = item.find("div", class_="prew_params")
                        product_screen_specs = {}
                        if product_screen_info_block:
                            for li in product_screen_info_block.find_all("li"):
                                key = li.find("b").get_text(strip=True).replace(":", "").replace("&nbsp;", "")
                                value = li.find("i").get_text(strip=True)
                                product_screen_specs[key] = value

                        all_products = f"{product_name}\n" \
                                       f"{product_image}\n" \
                                       f"Ссылка: {product_link}\n" \
                                       f"Цена (со скидкой): {product_price_new}\n" \
                                       f"Цена (без скидки): {product_price_old}\n" \
                                       f"Диагональ экрана: {product_screen_specs["Диагональ экрана"]}\n" \
                                       f"Разрешение экрана: {product_screen_specs["Разрешение экрана"]}\n" \
                                       f"Технология экрана: {product_screen_specs["Технология экрана"]}\n" \
                                       f"Частота обновления матрицы: {product_screen_specs["Частота обновления матрицы"]}\n" \
                                       f"Наличие SmartTV: {product_screen_specs["Smart TV"]}\n" \
                                       f"Цвет: {product_screen_specs["Цвет"]}"

                        bot.send_message(chat_id, all_products)

                        cursor.execute('''
                                       INSERT INTO products (name, price_discounted)
                                       VALUES (?, ?)
                                       ''', (product_name, product_price_new))
                        connection.commit()

            cursor.close()
            connection.close()

            bot.send_message(chat_id, "Всё :)")
        elif message.text == "Не сейчас":
            bot.send_message(chat_id, f"До свидания :(")


bot.polling(none_stop=True)
