# -*- coding: utf-8 -*- 

import random

import requests

def point(event, context):
    print(event)
    if event["message"]["text"][0] == "/":
        words = event["message"]["text"].split()
        command = words[0][1:]
        if command == "echo":
            send_message(event["message"]["from"]["id"], event["message"]["text"])
        elif command == "help":
            help_text = "Это вспомогательный текст. Здесь будет написано что и как со мной можно сделать"
            send_message(event["message"]["from"]["id"], help_text)
        elif command == "joke":
            JOKES_DICT = [
                "Шутка1",
                "Шутка2",
                "Шутка3"
            ]
            send_message(event["message"]["from"]["id"], random.choice(JOKES_DICT))
        else:
            send_message(event["message"]["from"]["id"], "Я не знаю эту команду")
    else:
        send_message(event["message"]["from"]["id"], "Введите команду")
    

def send_message(chat_id, text):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="569498492:AAEvy6yRzqkygb9DXpnPTOICbihG-rkq6rc",
        method="sendMessage"
    )
    data = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, data = data)
    print(r.json())



"""import requests
import datetime

token = '569498492:AAEvy6yRzqkygb9DXpnPTOICbihG-rkq6rc'


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
"""
