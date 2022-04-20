from func import mul

# 1. Проверка умножения двух положительных чисел:
def test_mul_2positive():
    assert mul(10, 2) == 20

# 2. Проверка умножения положительного числа на отрицательное:
def test_mul_positive_and_negative():
    assert mul(10, -2) == -20

# 3. Проверка умножения отрицательного числа на положительное:
def test_mul_negative_and_positive():
    assert mul(-10, 2) == -20

# 4. Проверка умножения нуля на положительное число:
def test_mul_zero_and_positive():
    assert mul(0, 2) == 0

# 5. Проверка умножения положительного числа на ноль:
def test_mul_positive_and_zero():
    assert mul(2, 0) == 0

# 6. Проверка умножения отрицательно числа на ноль:
def test_mul_negative_and_zero():
    assert mul(-2, 0) == 0

# 7. Проверка умножения нуля на отрицательное число:
def test_mul_zero_and_negative():
    assert mul(0, -2) == 0

# 8. Проверка умножения двух одинаковых положительных чисел:
def test_the_same_positive():
    assert mul(2, 2) == 4

# 9. Проверка умножения двух одинаковых отрицательных чисел:
def test_the_same_negative():
    assert mul(-2, -2) == 4

# 10. Проверка умножения ноль на ноль:
def test_zero():
    assert mul(0, 0) == 0