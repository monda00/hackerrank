'''
Word Order
'''

from collections import OrderedDict

if __name__ == '__main__':
    word_set = OrderedDict()
    for _ in range(int(input())):
        word = input()
        word_set.setdefault(word, 0)
        word_set[word] += 1

    print(len(word_set))
    print(*word_set.values())

