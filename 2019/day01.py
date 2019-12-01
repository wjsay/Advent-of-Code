import math

def read_text(filename):
    data = []
    with open(filename, 'r') as fin:
        for line in fin.readlines():
            line = line.strip('\n')
            data.append(int(line))
    return data

def solution1(data):
    ret = 0
    for v in data:
        a = math.floor(v / 3) - 2
        ret += a
    print(ret)

def solution2(data):
    ret = 0
    for v in data:
        a = 0
        while v > 0:
            v = math.floor(v / 3) - 2
            if v > 0:
                a += v
        # print(a)
        ret += a
    print(ret)

def main():
    filename = 'src/input.txt'
    # filename = 'src/tmp.txt'
    data = read_text(filename)
    # solution1(data)
    solution2(data)

if __name__ == "__main__":
    main()
