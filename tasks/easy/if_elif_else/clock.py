"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Электронные часы
Электронные часы показывают время в формате ЧЧ:ММ:СС

Отредактировать функцию get_seconds, которая принимает 3 аргумента:
    - h - количество часов
    - m - количество минут
    - s - количество секунд
таким образом, чтобы она возвращала общее количество секунд с 00:00:00

Если пользователь передает недопустимые значения, то функция должна вернуть
строку:
    - "Ошибка. Допустимое значение для часов 0..23"
    - "Ошибка. Допустимое значение для минут 0..59"
    - "Ошибка. Допустимое значение для секунд 0..59"
в зависимости от того, где была допущена ошибка

ПРИМЕРЫ
--------------------------------------------------------------------------------
- get_seconds(2, 13, 25) -> 8005
- get_seconds(23, 0, 43) -> 82843
- get_seconds(25, 0, 43) -> "Ошибка. Допустимое значение для часов 0..23"
- get_seconds(23, 61, 43) -> "Ошибка. Допустимое значение для минут 0..59"
- get_seconds(23, 0, -1) -> "Ошибка. Допустимое значение для секунд 0..59"
"""
from typing import Union


def get_seconds(h: int, m: int, s: int) -> Union[int, str]:
    """Возвращает количество секунд от 00:00:00 в зависимости от переданного
    времени на электронных часах

    :param h: часы
    :type h: int

    :param m: минуты
    :type m: int

    :param s: секунды
    :type s: int

    :return: количество сеекунд от 00:00:00
    :rtype: int
    """
    if h in range(0, 24):
        h = h * 60 * 60
    else:
        return "Ошибка. Допустимое значение для часов 0..23"
    if m in range(0, 60):
        m = m * 60
    else:
        return "Ошибка. Допустимое значение для минут 0..59"
    if s in range(0, 60):
        s = s
    else:
        return "Ошибка. Допустимое значение для секунд 0..59"

    result = h + m + s
    return result


if __name__ == '__main__':
    h_val = int(input('Введите количество часов h: '))
    m_val = int(input('Введите количество минут m: '))
    s_val = int(input('Введите количество секунд s: '))
    print(f'Общее кол-во секунд с 00:00:00: '
          f'{get_seconds(h_val, m_val, s_val)}')
