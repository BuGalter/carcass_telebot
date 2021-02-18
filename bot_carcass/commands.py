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

"""Модуль соджержит команды бота

Основное назначение - хранение доступных боту команд

Global variable
---------------
BOT_COMMANDS : dict
    Словарь для хранения команд бота
"""

BOT_COMMANDS = {'/start': 'Добрый день! Чем могу Вам помочь?',
                '/help': 'Список доступных команд:\n /start\n/help\n/settings',
                '/settings': 'Список возможных настроек:\n',
                'not_command': 'Команды:\n /start\n/help\n/settings'}
