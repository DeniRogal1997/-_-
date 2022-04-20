from func import div


# 1. Проверка деления двух положительных чисел:
def test_div_2positive():
    assert div(10, 2) == 5

# 2. Проверка деления положительного числа на отрицательное:
def test_div_positive_and_negative():
    assert div(10, -2) == -5

# 3. Проверка деления отрицательного числа на положительное:
def test_div_negative_and_positive():
    assert div(-12, 2) == -6

# 4. Проверка деления нуля на положительное число:
def test_div_zero_and_posititve():
    assert div(0, 2) == 0

# 5. Проверка деления нуля на отрицательное число:
def test_div_zero_and_negative():
    assert div(0, -2) == 0

# 6. Проверка деления двух одинаковых положительных чисел:
def test_div_the_same_positive():
    assert div(2, 2) == 1

# 7. Проверка деления двух одинаковых отрицательных чисел:
def test_div_the_same_negative():
    assert div(-2, -2) == 1