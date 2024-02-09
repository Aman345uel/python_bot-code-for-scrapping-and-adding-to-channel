# Name: Amanuel Merid Section: A 
from bs4 import BeautifulSoup
import requests
import io
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

bot_token = '6717237649:AAHofPLIUAdhaSsrdSgaHA44eIzLWpxLuH8'
channel_chat_id = '-1002015384167'
user_chat_id = '907940199'

response = requests.get('https://www.ethiopianreporter.com/')
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('div', class_='td_block_inner td-mc1-wrap')
titles = soup.find_all('h3', class_='entry-title td-module-title')
images = soup.find_all('div', class_='td-image-container')

def send_to_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, params=params)
    return response.json()

for index, article in enumerate(articles):
    title = titles[index].get_text(strip=True)

    link = article.find('a', href=True)['href']

    image_element = images[index].find('img')
    if image_element:
        image_url = image_element.get('src')
    else:
        image_url = "No image available"

    text = f"Title: {title}\nLink: {link}\nImage: {image_url}\n"

    send_to_telegram(bot_token, channel_chat_id, text)

    send_to_telegram(bot_token, user_chat_id, text)


    time.sleep(4)
