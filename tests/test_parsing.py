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
get_data_update()
    функция возвращает список, который содержит сообщения,
    которые не были прочитанны
get_id_update()
    получает номер обновления из полученного словаря
get_chat_id()
    получает номер текущего чата
get_name_user()
    получает имя юзера от которого пришло сообщение
get_text_update()
    функция получает текст сообщения от пользователя
parsing_text_update()
    функция проверяет, есть ли в тексте команды, которые знает бот,
    если да то возвращает текст, соответствующий команде, если нет,
    то стандартное сообщение в котором содержиться перечень команд.
"""
