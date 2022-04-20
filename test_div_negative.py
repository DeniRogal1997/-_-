from func import div
import pytest


#ЗДЕСЬ БУДУТ ОПИСАНЫ НЕГАТИВНЫЕ ТЕСТЫ ДЛЯ ДЕЛЕНИЯ
# 1. Проверка деления положительного числа на ноль:
def test_div_positive_and_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)


# 2. Проверка деления отрицательного числа на ноль:
def test_div_negative_and_zero():
    with pytest.raises(ZeroDivisionError):
        div(-10, 0)


# 3. Проверка деления ноль на ноль:
def test_div_zero_and_zero():
    with pytest.raises(ZeroDivisionError):
        div(0, 0)