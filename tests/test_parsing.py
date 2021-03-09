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

"""Модуль для хранения методов необходимых для получения данных.

Основное назначение - получение данных из ответа от апи телеграм,
которые необходимы для работы бота

Functions
---------
test_parsing_text_update()
    определяем список, содержащий, доступные команды боту
    и произвольные. В случае, если команда определенна для бота получаем
    текст, который связан с командой, если команда не известна,
    то возвращаем стандартный ответ

get_data_update()
get_id_update()
get_chat_id()
get_name_user()
get_text_update()
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
