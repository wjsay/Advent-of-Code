
import re
from collections import defaultdict
import numpy as np


def main():
    fin = open('input.txt', 'rt')
    regex = re.compile(r'\[(.*)] (.*)')
    recs = [regex.match(line.strip('\n')).groups() for line in fin.readlines()]
    recs.sort()
    fin.close()
    id = -1; st = 0; t = np.zeros(60, dtype=int)
    sum = defaultdict(int)
    for rec in recs:
        if rec[1] == 'falls asleep':
            st = int(rec[0].split(':')[-1])
        elif rec[1] == 'wakes up':
            ed = int(rec[0].split(':')[-1])
            sum[id] += ed - st
            if id == 857:
                t[st:ed] += 1
        else:
            id = int(rec[1].split()[1][1:])
    maxid = max(sum, key=sum.get)
    print(maxid)
    for i in range(len(t)):
        if t[i] == t.max():
            print(i * maxid)



if __name__ == '__main__':
    main()
# 3533 39

'''
[1518-07-16 00:00] Guard #3209 begins shift
[1518-03-18 23:57] Guard #857 begins shift
[1518-05-05 00:22] wakes up
[1518-03-20 00:25] wakes up
[1518-04-20 00:52] wakes up
[1518-04-11 00:01] Guard #3259 begins shift
[1518-09-17 00:58] wakes up
[1518-05-03 00:53] wakes up
[1518-10-27 00:44] falls asleep
[1518-06-03 00:52] wakes up
[1518-03-31 00:02] Guard #1571 begins shift
[1518-03-30 00:56] wakes up
[1518-07-06 23:54] Guard #857 begins shift
'''