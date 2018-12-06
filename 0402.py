
import re
from collections import defaultdict
import numpy as np

def main():
    fin = open('input.txt', 'rt')
    regex = re.compile(r'\[(.*)] (.*)')
    recs = [regex.match(line.strip('\n')).groups() for line in fin.readlines()]
    recs.sort()
    fin.close()
    id = -1; st = 0;
    sum = dict()
    for rec in recs:
        if rec[1] == 'falls asleep':
            st = int(rec[0].split(':')[-1])
        elif rec[1] == 'wakes up':
            ed = int(rec[0].split(':')[-1])
            t = sum.get(id)
            t[st: ed] += 1
        else:
            id = int(rec[1].split()[1][1:])
            if id not in sum:
                sum[id] = np.zeros(60, dtype='int32')
    maxV = 0
    for t in sum.values():
        maxV = max(maxV, t.max())
    print(max(sum))
    for id in sum.keys():
        if sum[id].max() == maxV:
            print(id)
            t = sum[id]
            for m in range(60):
                if t[m] == maxV:
                    print(m)
                    print(m * id)


if __name__ == '__main__':
    main()
