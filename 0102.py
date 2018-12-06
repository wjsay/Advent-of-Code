
def main():

    with open('input.txt', 'rt') as fin:
        sum = 0
        s = {sum}
        while True:
            fin.seek(0)
            for line in fin.readlines():
                sum += int(line)
                if sum in s:
                    print(sum)
                    return
                else:
                    s.add(sum)


if __name__ == '__main__':
    main()