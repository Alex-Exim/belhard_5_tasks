"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая проверит, все ли элементы в списке уникальны

ПРИМЕРЫ
--------------------------------------------------------------------------------
is_unique([2, 1, 5, 4, 7]) -> True
is_unique([2, 1, 5, 4, 2]) -> False
"""


def is_unique(array: list) -> bool:
    new_array = set(array)
    if len(array) == len(new_array):
        result = True
    else:
        result = False
    return result


if __name__ == '__main__':
    assert is_unique([2, 1, 5, 4, 7])
    assert not is_unique([2, 1, 5, 4, 2])
    print('Решено!')
