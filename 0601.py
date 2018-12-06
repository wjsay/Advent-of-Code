
MAXN = 360
m = [[0] * MAXN for _ in range(MAXN)]


def bfs(r, c, val):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    que = [(r, c)]
    cnt = 1; fg = False
    m[r][c] = 0
    while que:
        r, c = que[0]; que.remove(que[0])
        for dir in dirs:
            rr = r + dir[0]
            cc = c + dir[1]
            if cc < 0 or cc >= MAXN or rr < 0 or rr >= MAXN:
                fg = True; continue
            if m[rr][cc] == val:
                que.append((rr, cc))
                m[rr][cc] = 0
                cnt += 1
    return -1 if fg else cnt


def main():
    global m, MAXN
    with open('input.txt', 'rt') as fin:
        points = []
        for i, line in enumerate(fin.readlines()):
            x, y = map(int, line.strip('\n').split(', '))
            points.append((x, y, i + 1))
            m[y][x] = i + 1
    for r in range(MAXN):
        for c in range(MAXN):
            if m[r][c] != 0: continue
            minV = 0x3f3f3f3f; cnt = 0; k_ = 0
            for k in range(len(points)):
                d = abs(points[k][0] - c) + abs(points[k][1] - r)
                if minV > d:
                    minV, cnt, k_ = d, 1, k
                elif minV == d:
                    cnt += 1
            if cnt == 1:
                m[r][c] = points[k_][2]
    maxV = 0
    for r in range(MAXN):
        for c in range(MAXN):
            if m[r][c] != 0:
                maxV = max(maxV, bfs(r, c, m[r][c]))
        #     print(m[r][c], end=' ')
        # print()
    print(maxV)


if __name__ == '__main__':
    main()