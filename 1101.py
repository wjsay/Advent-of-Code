

def solution1(data):
    serial_number = data
    width = 301
    matrix = [[0] * width for _ in range(width)]
    ans_y = ans_x = 0; total = -9999999
    for Y in range(1, width):
        for X in range(1, width):
            rack_ID = X + 10
            matrix[Y][X] = (rack_ID * Y + serial_number) * rack_ID // 100 % 10 - 5
    for Y in range(1, width - 3):
        for X in range(1, width - 3):
            tmp = sum(matrix[Y][X:X+3]) + sum(matrix[Y+1][X:X+3]) + sum(matrix[Y+2][X:X+3])
            if tmp > total:
                total = tmp
                ans_y = Y
                ans_x = X
    print(ans_x, ans_y)


def main():
    solution1(1788)

if __name__ == '__main__':
    main()