import pytest


# Проверяем корректность деления
def test_division():
    assert 10 / 2 == 5


# Проверяем, что вызов функции вернет ошибку деления на ноль
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert 10 / 0


# проверяем остаток от деления
@pytest.mark.parametrize("a,b,expected", [(10, 2, 0),
                                          (20, 4, 0),
                                          (13, 2, 1)])
def test_mod(a, b, expected):
    assert a % b == expected


# проверяем, что у всех элементов кортежа тип int
def test_tuple_type():
    testing_tuple_first = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for i in testing_tuple_first:
        assert type(i) == int


# проверяем количество элементов кортежа
def test_tuple_length():
    testing_tuple_second = (1, 2, 3)
    assert len(testing_tuple_second) == 3


# проверяем сумму элементов кортежа
def test_elements_sum():
    testing_tuple_third = (1, 2, 15)
    assert sum(testing_tuple_third) == 18
