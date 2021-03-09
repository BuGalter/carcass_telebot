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

"""Пакет содержит каркас простого чат-бота для телеграм.

bot.py : Основной, запускаемый модуль, содержит код бота.

urls.py : Модуль содержит все урлы. функции для получения токена и
базового урла. Также функции для получения урлов, которые
необходимы для работы бота.

checks.py : Модуль содержит функции, которые служат для проверки
корректности данных, используемых ботом в работе.

parsing.py : получение данных из ответа от апи телеграм,
которые необходимы для работы бота

bot_methods.py : хранение методов бота для работы с апи телеграм

Valera WarDoc [https://github.com/BuGalter]
wardoc78@gmail.com
License: Apache License 2.0
version: "1.0.0"
"""
