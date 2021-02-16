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
from urls import get_token


def main():
    token = get_token()
    if token is None:
        logging.warning('An error occurred while running the bot!')
        return
    print(token)


if __name__ == '__main__':
    print('Bot - start work!')
    main()
    print('Bot - finished work!')
