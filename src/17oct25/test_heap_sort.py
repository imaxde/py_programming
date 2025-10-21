from heap_sort import heap_sort
import pytest
import random

def test_simple():
    assert heap_sort([3, 2, 1, 5, 10, 8]) == [1, 2, 3, 5, 8, 10]

def test_short_list():
    assert heap_sort([42, 0]) == [0, 42]

def test_long_list():
    a = [93, 49, 39, 24, 69, 72, 90, 38, 55, 24, 63, 23, 39, 84, 35, 68, 80, 17, 12, 94, 69, 37, 97, 89, 16, 53, 96, 13]
    b = [12, 13, 16, 17, 23, 24, 24, 35, 37, 38, 39, 39, 49, 53, 55, 63, 68, 69, 69, 72, 80, 84, 89, 90, 93, 94, 96, 97]
    heap_sort(a)
    assert a == b

def test_list_of_strings():
    assert heap_sort(["p", "y", "t", "h", "o", "n"]) == ['h', 'n', 'o', 'p', 't', 'y']

def test_self():
    assert heap_sort([40, 8, 25, 9, 37, 23, 41, 18, 35, 24]) == heap_sort([40, 8, 25, 9, 37, 23, 41, 18, 35, 24])

@pytest.mark.parametrize(
    ["input_data", "expected_out"],
    [
        ([1, 3, 2], [1, 2, 3]),
        ([10**10, 10**9, 10**5, 10**8, 10**2, 10**7], [10**2, 10**5, 10**7, 10**8, 10**9, 10**10]),
        ([651, -86, -152, 384, 245, 428, -29, -839, -575, -472], [-839, -575, -472, -152, -86, -29, 245, 384, 428, 651]),
        ([313, 665, -641, -435, -819, -420, 801, 208], [-819, -641, -435, -420, 208, 313, 665, 801]),
        ([-5505, 9828, 9045, 969, 1508, -8066, -8690], [-8690, -8066, -5505, 969, 1508, 9045, 9828]),
        ([-35.120, 28.864, 54.075, -5.354, 57.778, 43.898], [-35.120, -5.354, 28.864, 43.898, 54.075, 57.778]),
        ([1.3, 1.2, 1.1, 1.0], [1.0, 1.1, 1.2, 1.3]),
    ]
)
def test_another(input_data, expected_out):
    assert heap_sort(input_data) == expected_out

@pytest.mark.xfail(raises=TypeError)
def test_incorrect_type():
    assert heap_sort(1)

def test_empty_list():
    assert heap_sort([]) == []

@pytest.fixture()
def random_int_list():
    random_list = random.sample(range(-200, 200), 150)
    return random_list

def test_property_python_sort(random_int_list):
    a = sorted(random_int_list)
    b = heap_sort(random_int_list)
    assert a == b

