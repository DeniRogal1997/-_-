from func import sum


# 1. Проверка сложения двух положительных чисел, результат положительный:
def test_sum_2positive():
    assert sum(10, 2) == 12

# 2. Проверка сложения отрицательного числа и положительного, результат отрицательный:
def test_sum_negative_and_positive():
    assert sum(-15, 2) == -13

# 3. Проверка сложения одного отрицательного числа и одно положительного, результат положительный:
def test_sum_negative_and_positive_result_positive():
    assert sum(15, -2) == 13

# 4. Проверка сложения положительного и отрицательного числа, результат = 0:
def test_sum_negative_and_positive_result_zero():
    assert sum(15, -15) == 0

# 5. Проверка сложения положительного числа и нуля:
def test_sum_positive_and_zero():
    assert sum(15, 0) == 15

# 6. Проверка сложения нуля и положительного числа:
def test_sum_zero_and_positive():
    assert sum(0, 15) == 15

# 7. Проверка сложения отрицательного числа и нуля:
def test_sum_negative_and_zero():
    assert sum(-15, 0) == -15

# 8. Проверка сложения нуля и отрицательного числа:
def test_sum_zero_and_negative():
    assert sum(0, -15) == -15

# 9. Проверка сложения двух одинаковых положительных чисел:
def test_sum_the_same_positive():
    assert sum(10, 10) == 20

# 10. Проверка сложения двух одинаковых отрицательных чисел:
def test_sum_the_same_negative():
    assert sum(-10, -10) == -20

# 11. Сложения двух нулей:
def test_sum_zero():
    assert sum(0, 0) == 0