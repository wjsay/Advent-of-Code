
MAXN = 360 + 200; OFFSET= 100; MAXV = 10000
m = [[0] * MAXN for _ in range(MAXN)]


def main():
    global m, MAXN
    with open('input.txt', 'rt') as fin:
        points = []
        for i, line in enumerate(fin.readlines()):
            x, y = map(int, line.strip('\n').split(', '))
            points.append((x + OFFSET, y + OFFSET))
    cnt = 0
    for r in range(MAXN):
        for c in range(MAXN):
            d = 0
            for (x, y) in points:
                d += abs(r - y) + abs(c - x)
                if d >= MAXV: break
            if d < MAXV: cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()