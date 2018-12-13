
import re


def read_txt(filename):
    data = []
    with open(filename, 'r') as fin:
        for line in fin.readlines():
            data.append(line.strip('\n'))
    return data


dir_dict = {'^': 0, 'v':1, '<':2, '>': 3,}
dir_change = [
    {0: 2, 1: 3, 2: 1, 3: 0},  # 左拐
    {0: 0, 1: 1, 2: 2, 3: 3},  # 直行
    {0: 3, 1: 2, 2: 0, 3: 1},  # 右拐
]
m = []
carts = []
xy_set = set()


def check(cart):
    if (cart[1], cart[0]) in xy_set:
        return True
    else:
        return False


def error(flag=0):
    print('error', flag)
    exit(0)


def move(cart):
    global m
    cur_y, cur_x, cur_dir, _ = cart[0], cart[1], cart[2], cart[3]
    try:
        ch = m[cur_y][cur_x]
    except:
        print(len(m), len(m[0]))
        print(cur_y, cur_x)
        exit(0)
    if ch == '/':
        if cur_dir == 2:  # <
            cart[0] += 1
            cart[2] = 1
        elif cur_dir == 0:  # ^
            cart[1] += 1
            cart[2] = 3
        elif cur_dir == 3:  # >
            cart[0] -= 1
            cart[2] = 0
        elif cur_dir == 1:  # v
            cart[1] -= 1
            cart[2] = 2
        else: print(cur_dir); error(1)
    elif ch == '\\':
        if cur_dir == 0:  # ^
            cart[1] -= 1
            cart[2] = 2
        elif cur_dir == 3:  # >
            cart[0] += 1
            cart[2] = 1
        elif cur_dir == 1:  # v
            cart[1] += 1
            cart[2] = 3
        elif cur_dir == 2:  # <
            cart[0] -= 1
            cart[2] = 0
        else: error(2)
    elif ch == '|':
        if cur_dir == 0:  # ^
            cart[0] -= 1
        elif cur_dir == 1:  # v
            cart[0] += 1
        else: print(cur_dir); error(3)
    elif ch == '-':
        if cur_dir == 2:  # <
            cart[1] -= 1
        elif cur_dir == 3:  # >
            cart[1] += 1
        else: print(cur_dir); error(4)
    elif ch == '+':
        cart[2] = dir_change[cart[3]][cur_dir]  # 下一个方向
        if cart[2] == 0:  # ^
            cart[0] -= 1
        elif cart[2] == 1:  # v
            cart[0] += 1
        elif cart[2] == 2:  # <
            cart[1] -= 1
        elif cart[2] == 3:  # >
            cart[1] += 1
        else: error(5)
        cart[3] = (cart[3] + 1) % 3


def solution1(data):
    global carts, xy_set
    while True:
        for cart in carts:
            xy_set.remove((cart[1], cart[0]))
            move(cart)
            if check(cart):
                print(cart[1], cart[0], sep=',')
                return
            else:
                xy_set.add((cart[1], cart[0]))


def solution2(data):
    pass


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    global m, carts, xy_set
    m = [list(line) for line in data]
    for Y, row in enumerate(m):
        for X, ch in enumerate(list(row)):
            if ch in dir_dict:
                carts.append([Y, X, dir_dict[ch], 0])  # 行，列，方向，改变方向
                xy_set.add((X, Y))
    for cart in carts:
        if cart[2] in [0, 1]:
            m[cart[0]][cart[1]] = '|'
            if cart[1] - 1 >= 0 and m[cart[0]][cart[1] - 1] == '-':
                m[cart[0]][cart[1]] = '+'
        else:
            m[cart[0]][cart[1]] = '-'
            if cart[0] - 1 >= 0 and m[cart[0] - 1][cart[1]] == '|':
                m[cart[0]][cart[1]] = '+'
    solution1(data)


if __name__ == '__main__':
    main()
