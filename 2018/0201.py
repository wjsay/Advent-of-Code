
from collections import defaultdict


def work(letter):
    d = defaultdict(int)
    for ch in list(letter):
        d[ch] += 1
    t2 = 1 if 2 in d.values() else 0
    t3 = 1 if 3 in d.values() else 0
    return t2, t3


def main():
    with open('input.txt', 'rt') as fin:
        two, three = (0, 0)
        for letter in fin.readlines():
            (t2, t3) = work(letter)
            two += t2
            three += t3
        print(two * three)


if __name__ == '__main__':
    main()