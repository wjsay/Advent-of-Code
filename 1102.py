
import numpy as np

serial_number = 1788  # 改这里
width = 301
m = np.zeros((width, width), dtype='int32')
for Y in range(1, width):
    for X in range(1, width):
        rack_ID = X + 10
        m[Y, X] = (rack_ID * Y + serial_number) * rack_ID // 100 % 10 - 5


def work(data):
    ans_y = ans_x = 0;
    total = -9999999
    for Y in range(1, width - data):
        for X in range(1, width - data):
            tmp = m[Y:Y+data, X:X+data].sum()
            if tmp > total:
                total = tmp
                ans_y = Y
                ans_x = X
    return [ans_x, ans_y, data, total]


def main():
    maxV = 0; ans = []
    for size in range(1, 300):
        tmp = work(size)
        if tmp[3] > maxV:
            print(tmp)
            maxV = tmp[3]
            ans = tmp
    print("ans", tmp)



if __name__ == '__main__':
    main()