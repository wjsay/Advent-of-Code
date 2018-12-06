
def main():
    with open('input.txt', 'rt') as fin:
        data = [line.strip('\n') for line in fin.readlines()]
        if not data: return
        for c in range(len(data[0])):
            lst = [data[r][0:c] + data[r][c + 1:] for r in range(len(data))]
            lst.sort()
            for i in range(1, len(lst)):
                if lst[i] == lst[i - 1]:
                    print(lst[i])
                    return


if __name__ == '__main__':
    main()