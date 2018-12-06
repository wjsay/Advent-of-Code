
import numpy as np


def main():
    with open('input.txt', 'rt') as fin:
        n = 1001
        m = np.zeros((n, n), dtype='int32')
        for line in fin.readlines():
            line.strip('\n')
            cr, wh = line.split(' ')[2:]
            c, r = map(int, str(cr.strip(':')).split(','))
            w, h = map(int, str(wh).split('x'))
            m[r:r+h, c:c+w] += 1
        print(len(m[m > 1]))


if __name__ == '__main__':
    main()