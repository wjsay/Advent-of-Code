
def main():
    with open('input.txt', 'rt') as fin:
        ans = 0
        for line in fin.readlines():
            ans += int(line)
        print(ans)


if __name__ == '__main__':
    main()