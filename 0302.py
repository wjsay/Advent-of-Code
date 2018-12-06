
import numpy as np


def main():
    with open('input.txt', 'rt') as fin:
        n = 1001 # 矩阵的阶
        m = np.zeros((n, n), dtype='int32')
        ids = cs = rs = ws = hs = []
        for line in fin.readlines():
            line.strip('\n')
            id, _, cr, wh = line.split(' ')
            c, r = map(int, str(cr.strip(':')).split(','))
            w, h = map(int, str(wh).split('x'))
            m[r:r+h, c:c+w] += 1
            ids.append(id[1:]); cs.append(c); rs.append(r); ws.append(w); hs.append(h)
        for i in range(len(ids)):
            id = ids[i]; r = rs[i]; h = hs[i]; c = cs[i]; w = ws[i]
            tmp = m[r:r + h, c:c + w]
            if len(tmp[tmp > 1]) == 0:
                print(id)
                # break


if __name__ == '__main__':
    main()