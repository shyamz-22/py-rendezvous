import random
import string
from collections import Counter


def count_alphabet(value: str):
    for letter in string.ascii_lowercase:
        occurances = value.count(letter)
        if occurances > 0:
            print(f'`{letter}` occurs {occurances} time(s)')


def random_string(chars, length):
    return ''.join(random.choices(chars, k=length))


if __name__ == '__main__':
    a_string = random_string(chars=string.ascii_lowercase, length=10)
    count_alphabet(a_string)

    longest_word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    print('Longest Word: ', longest_word)
    c = Counter(longest_word)
    print('counter: ', c)
    print('')
    print('top 5: ', c.most_common(5))
