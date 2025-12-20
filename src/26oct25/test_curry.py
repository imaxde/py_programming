import pytest
from curry import curry, uncurry


def test_curry_two_args():
    """Тест каррирования функции с двумя аргументами"""
    def add(a, b):
        return a + b
    
    curried_add = curry(add, 2)
    
    # Постепенное применение аргументов
    add_5 = curried_add(5)
    assert add_5(3) == 8
    
    # Вызов с полным набором аргументов сразу
    assert curried_add(10, 20) == 30


def test_curry_three_args():
    """Тест каррирования функции с тремя аргументами"""
    def multiply_add(a, b, c):
        return a * b + c
    
    curried_func = curry(multiply_add, 3)
    
    # Постепенное применение по одному аргументу
    step1 = curried_func(2)
    step2 = step1(3)
    assert step2(4) == 10
    
    # Частичное применение с несколькими аргументами сразу
    assert curried_func(2, 3)(4) == 10
    
    # Полный вызов сразу
    assert curried_func(2, 3, 4) == 10


def test_curry_four_args():
    """Тест каррирования функции с четырьмя аргументами"""
    def complex_op(a, b, c, d):
        return a + b * c - d
    
    curried_func = curry(complex_op, 4)
    
    # Постепенное применение по одному аргументу
    assert curried_func(1)(2)(3)(4) == 3  # 1 + 2*3 - 4 = 3
    
    # Частичное применение с несколькими аргументами сразу
    assert curried_func(1, 2)(3)(4) == 3
    assert curried_func(1, 2, 3)(4) == 3
    
    # Полный вызов сразу
    assert curried_func(1, 2, 3, 4) == 3


def test_curry_wrong_arg_count():
    """Тест ошибки при неверном количестве аргументов"""
    def add(a, b):
        return a + b
    
    with pytest.raises(Exception, match="Неверное количество аргументов"):
        curry(add, 3)
    
    with pytest.raises(Exception, match="Неверное количество аргументов"):
        curry(add, 1)


def test_uncurry_two_args():
    """Тест разкаррирования функции с двумя аргументами"""
    def curried_add(a):
        def inner(b):
            return a + b
        return inner
    
    uncurried_add = uncurry(curried_add, 2)
    assert uncurried_add(5, 3) == 8
    assert uncurried_add(10, 20) == 30


def test_uncurry_three_args():
    """Тест разкаррирования функции с тремя аргументами"""
    def curried_func(a):
        def step1(b):
            def step2(c):
                return a * b + c
            return step2
        return step1
    
    uncurried_func = uncurry(curried_func, 3)
    assert uncurried_func(2, 3, 4) == 10


def test_uncurry_four_args():
    """Тест разкаррирования функции с четырьмя аргументами"""
    def curried_func(a):
        def step1(b):
            def step2(c):
                def step3(d):
                    return a + b * c - d
                return step3
            return step2
        return step1
    
    uncurried_func = uncurry(curried_func, 4)
    assert uncurried_func(1, 2, 3, 4) == 3


def test_curry_uncurry_roundtrip():
    """Тест обратимости: uncurry(curry(f)) == f"""
    def add(a, b):
        return a + b
    
    curried = curry(add, 2)
    uncurried = uncurry(curried, 2)
    
    assert uncurried(5, 3) == add(5, 3)
    assert uncurried(10, 20) == add(10, 20)


def test_curry_uncurry_roundtrip_three_args():
    """Тест обратимости для функции с тремя аргументами"""
    def multiply_add(a, b, c):
        return a * b + c
    
    curried = curry(multiply_add, 3)
    uncurried = uncurry(curried, 3)
    
    assert uncurried(2, 3, 4) == multiply_add(2, 3, 4)
    assert uncurried(5, 6, 7) == multiply_add(5, 6, 7)


def test_curry_with_zero():
    """Тест каррирования с нулевыми значениями"""
    def add(a, b):
        return a + b
    
    curried_add = curry(add, 2)
    assert curried_add(0, 0) == 0
    assert curried_add(0)(5) == 5
    assert curried_add(5)(0) == 5


def test_curry_with_negative():
    """Тест каррирования с отрицательными значениями"""
    def subtract(a, b):
        return a - b
    
    curried_subtract = curry(subtract, 2)
    assert curried_subtract(10, 3) == 7
    assert curried_subtract(-5)(-3) == -2
    assert curried_subtract(0)(-10) == 10

