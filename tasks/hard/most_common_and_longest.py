"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""
from collections import Counter


def common_and_longest(text: str) -> tuple:
    # counter = Counter(text.split(" "))
    # common, longest = counter.most_common(1)[0][0], max(counter.keys())
    words = text.split(" ")
    counter = {}
    for word in words:
        # val = counter.get(word, 0)
        val = counter.setdefault(word, 0)
        counter[word] = val + 1

    common = ""
    longest = ""

    for word, count in counter.items():
        if count > counter.get(common, 0):
            common = word
        if len(word) > len(longest):
            longest = word
    return common, longest



if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
