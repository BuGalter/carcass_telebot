"""Основной, запускаемый модуль, содержит код бота

Основное назначение -

Global variable
---------------


Functions
---------
get_updates_longpolling()
    делает запрос к серверу телеграм для получения сообщений
"""
import logging
from urls import get_token, get_base_url, get_update_url


def main():
    token = get_token()
    if token is None:
        logging.warning('An error occurred while running the bot!')
        return
    base_url = get_base_url(token)
    print(base_url)
    get_update = get_update_url(base_url)
    print(get_update)


if __name__ == '__main__':
    print('Bot - start work!')
    main()
    print('Bot - finished work!')
