from func import sub


# 1. Проверка вычитания двух положительных чисел, результат положительный:
def test_sub_2positive():
    assert sub(10, 2) == 8

# 2. Проверка вычитания отрицательного числа и положительного, результат отрицательный:
def test_sub_negative_and_positive():
    assert sub(-15, 2) == -17

# 3. Проверка вычитания положительного и отрицательного, результат положительный:
def test_sub_negative_and_positive_result_positive():
    assert sub(15, -2) == 17

# 4. Проверка вычитания положительного и отрицательного числа:
def test_sub_negative_and_positive_result_zero():
    assert sub(15, -15) == 30

# 5. Проверка вычитания положительного числа и нуля:
def test_sub_positive_and_zero():
    assert sub(15, 0) == 15

# 6. Проверка вычитания нуля и положительного числа:
def test_sub_zero_and_positive():
    assert sub(0, 15) == -15

# 7. Проверка вычитания отрицательного числа и нуля:
def test_sub_negative_and_zero():
    assert sub(-15, 0) == -15

# 8. Проверка вычитания нуля и отрицательного числа:
def test_sub_zero_and_negative():
    assert sub(0, -15) == 15

# 9. Проверка вычитания двух одинаковых положительных чисел:
def test_sub_the_same_positive():
    assert sub(10, 10) == 0

# 10. Проверка вычитания двух одинаковых отрицательных чисел:
def test_sub_the_same_negative():
    assert sub(-10, -10) == 0

# 11. Вычитание двух нулей:
def test_sub_zero():
    assert sub(0, 0) == 0