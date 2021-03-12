# !/usr/bin/env python
# Copyright [2021] [Valeriy Yukubchik]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Модуль для тестирования parsing.py.

Основное назначение - набор тестов для функций, которые определенны в модуле
parsing.py

Functions
---------
test_parsing_text_update()
    определяем список, содержащий, доступные команды боту
    и произвольные. В случае, если команда определенна для бота получаем
    текст, который связан с командой, если команда не известна,
    то возвращаем стандартный ответ
get_data_update()
    определяем произвольный словарь, который содержит одним из
    ключей 'result', после вызова функции, проверяем, что она возвращает
    список из словаря равный заданному в словаре.
get_id_update()
    определяем произвольный словарь, который содержит одним из
    ключей 'update_id', после вызова функции, проверяем, что она возвращает
    из словаря число типа int равное 1.
get_chat_id()
    определяем произвольный словарь словарей словарей, который содержит
    ключи 'status_update', 'chat', 'id', определяем переменную, которая
    содержит ключ 'status_update' после вызова функции, проверяем, что
    она возвращает чиcло типа int равное 43
get_name_user()
    определяем произвольный словарь словарей, который содержит
    ключи 'status_update', 'chat', 'first_name', определяем переменную, которая
    содержит ключ 'status_update' после вызова функции, проверяем, что
    она возвращает строку равную buba.
get_text_update()
    определяем произвольный словарь словарей, который содержит
    ключи 'status_update', 'text', определяем переменную, которая
    содержит ключ 'status_update' после вызова функции, проверяем, что
    она возвращает строку равную my name buba.
get_message_status() - нет описаний в основном файле
    определяем произвольный словарь, после вызова функции
    мы должны получить из отсортированного списка ключей, первый
    в данном случае 'aaaaa'
get_message_id()- нет описаний в основном файле
    определяем произвольный словарь словарей, который содержит
    ключи 'status_update', 'messsage_id', определяем переменную, которая
    содержит ключ 'status_update' после вызова функции, проверяем, что
    она возвращает значение типа инт равное 10.
"""

from bot_carcass import parsing


def test_parsing_text_update():
    """Набор тестов для функции parsing_text_update.

    Описание - определяем список, содержащий, доступные команды боту
    и произвольные. В случае, если команда определенна для бота получаем
    текст, который связан с командой, если команда не известна,
    то возвращаем стандартный ответ
    """
    keys = ['/start', '/help', '/settings', 'command not', 'dsfghjksd']
    for key in keys:
        result = parsing.parsing_text_update(key)
        if key == '/start':
            assert result == 'Добрый день! Чем могу Вам помочь?'
        elif key == '/help':
            assert result == 'Список доступных команд:\n /start\n/help\n/settings'
        elif key == '/settings':
            result = parsing.parsing_text_update('not_command')
        else:
            assert result == 'Команды:\n /start\n/help\n/settings'


def test_get_data_update():
    """Тест для функции get_data_update.

    Описание - определяем произвольный словарь, который содержит одним из
    ключей 'result', после вызова функции, проверяем, что она возвращает
    список из словаря равный заданному в словаре.
    """
    results = {'result': [1, 2, 3, 4], 'not_result': 'sdjhfs'}
    res = parsing.get_data_update(results)
    assert res == [1, 2, 3, 4]
    assert type(res) == list


def test_get_id_update():
    """Тест для функции get_id_update.

    Описание - определяем произвольный словарь, который содержит одним из
    ключей 'update_id', после вызова функции, проверяем, что она возвращает
    из словаря число типа int равное 1.
    """
    results = {'update_id': 1, 'not_result': 'sdjhfs'}
    res = parsing.get_id_update(results)
    assert res == 1
    assert type(res) == int


def test_get_chat_id():
    """Тест для функции get_chat_id.

    Описание - определяем произвольный словарь словарей, который содержит
    ключи 'status_update', 'chat', 'id', определяем переменную, которая
    содержит ключ 'status_update' после вызова функции, проверяем, что
    она возвращает чиcло типа int равное 43
    """
    update = {'status_update': {'chat': {'id': 43}},
              'dfgddfgdf': {'sdfsdf': {'dsfsd': 'dsff'}}}
    st_update = 'status_update'
    res = parsing.get_chat_id(update, st_update)
    assert res == 43
    assert type(res) == int


def test_get_name_user():
    """Тест для функции get_name_user.

    Описание - определяем произвольный словарь словарей, который содержит
    ключи 'status_update', 'chat', 'first_name', определяем переменную, которая
    содержит ключ 'status_update' после вызова функции, проверяем, что
    она возвращает строку равную buba.
    """
    update = {'status_update': {'chat': {'first_name': 'buba'}},
              'dfgddfgdf': {'sdfsdf': {'dsfsd': 'dsff'}}}
    st_update = 'status_update'
    res = parsing.get_name_user(update, st_update)
    assert res == 'buba'
    assert type(res) == str


def test_get_text_update():
    """Тесты для функции get_text_update.

    Описание - определяем произвольный словарь словарей, который содержит
    ключи 'status_update', 'text', определяем переменную, которая
    содержит ключ 'status_update' после вызова функции, проверяем, что
    она возвращает строку равную my name buba.
    """
    update = {'status_update': {'text': 'my name buba', 'kjhk': 'gergegr'},
              'dfgddfgdf': {'text': 'my name buba', 'kjhk': 'gergegr'}}
    st_update = 'status_update'
    res = parsing.get_text_update(update, st_update)
    assert res == 'my name buba'
    assert type(res) == str


def test_get_message_status():
    """Тесты для функции get_message_status.

    Описание - определяем произвольный словарь, после вызова функции
    мы должны получить из отсортированного списка ключей, первый
    в данном случае 'aaaaa'
    """
    update = {'bbbbb': '2', 'cccccc': '3', 'aaaaa': '1', 'message': '4'}
    res = parsing.get_message_status(update)
    assert res == 'aaaaa'
    assert type(res) == str


def test_get_message_id():
    """Тесты для функции get_message_id.

    Описание - определяем произвольный словарь словарей, который содержит
    ключи 'status_update', 'messsage_id', определяем переменную, которая
    содержит ключ 'status_update' после вызова функции, проверяем, что
    она возвращает значение типа инт равное 10.
    """
    update = {'status_update': {'message_id': 10, 'kjhk': 25},
              'dfgddfgdf': {'mess_id': 10, 'kjhk': 25}}
    st_update = 'status_update'
    res = parsing.get_message_id(update, st_update)
    assert type(res) == int
    assert res == 10
