
import re, time, sys


def read_txt(filename):
    data = []
    regex = re.compile('position=<(.*),(.*)> velocity=<(.*),(.*)>')
    with open(filename, 'r') as fin:
        for line in fin.readlines():
            data.append(list(map(int, regex.match(line.strip('\n')).groups())))
    return data


def guess_solution1_answer(positions):
    xs = list(map(lambda e: e[0], positions))
    ys = list(map(lambda e: e[1], positions))
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    if max_x - min_x >= 8 and max_y - min_y >= 10: return False
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in positions:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')
    sys.stdout.flush()
    return True


def solution1(point_list):
    solution2_answer = 1
    while True:
        for point in point_list:
            point[0] += point[2]
            point[1] += point[3]
        if guess_solution1_answer(list(map(lambda p: (p[0], p[1]), point_list))):
            print(solution2_answer)
            print()
            print()
            time.sleep(1)
        solution2_answer += 1


def solution2(data):
    pass


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    # 信息高10，宽8
    solution1(data)
    # solution2(data)


if __name__ == '__main__':
    main()