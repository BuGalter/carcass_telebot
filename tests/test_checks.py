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

"""Модуль для тестирования checks.py.

Основное назначение - тестирование функций модуля checks.py

Functions
---------
test_check_url_none()
test_check_url()
test_check_status_code_not_200()
test_check_status_code()
"""

import pytest
from bot_carcass import checks


def test_check_url_none():
    """Тест функции check_url.

    Описание - в случае, когда урл не определен, проверяем, что
    был совершен выход из программы
    """
    url = None
    with pytest.raises(SystemExit) as excinfo:
        checks.check_url(url)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == 'Bot - finished work, not correct!!!'


def test_check_url():
    """Тест функции check_url.

    Описание - в случае, когда урл передан, работы программы продолжается,
    функция возвращает None
    """
    url = 'https://api.telegram.org/botallokey/'
    result = checks.check_url(url)
    assert result is None


def test_check_status_code_not_200():
    """Тест функции check_status_code.

    Описание - в случае когда код не равен 200, проверяем, что
    был совершен выход из программы
    """
    code = 400
    with pytest.raises(SystemExit) as excinfo:
        checks.check_status_code(code)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == 'Bot - finished work, not correct!!!'


def test_check_status_code():
    """Тест функции check_status_code.

    Описание - если код равен 200, работа программы продолжается,
    функция возвращает None
    """
    code = 200
    result = checks.check_status_code(code)
    assert result is None
