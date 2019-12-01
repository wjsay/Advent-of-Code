
def read_txt(filename):
    # 432 players; last marble is worth 71019 points
    data = []
    with open(filename, 'r') as fin:
        for line in fin.readlines():
            line = line.strip('\n').split()
            data.append([int(line[0]), int(line[6])])
    return data[0]


def solution1(data):
    player_count, last_marble = data[0], data[1]
    this_index = 1; this_marble = 2
    marble_list = [0, 1]; length = 2; this_player = 2
    palyer_score_list = [0] * player_count
    while this_marble <= last_marble:
        if this_marble % 23 == 0:
            palyer_score_list[this_player] += this_marble
            offset = 7 if 7 < length else 7 % length
            if this_index >= offset:
                this_index -= offset
            else:
                this_index = length - (offset - this_index)
            palyer_score_list[this_player] += marble_list[this_index]
            marble_list.remove(marble_list[this_index])
            length -= 1
        else:
            this_index += 2
            if this_index == length:
                this_index = length
            elif this_index == length + 1:
                this_index = 1
            marble_list.insert(this_index, this_marble)
            length += 1
        this_marble += 1
        this_player = (this_player + 1) % player_count
    print(max(palyer_score_list))


def solution2(data):
    player_count, last_marble = data[0], data[1] * 100
    this_index = 1; this_marble = 2
    marble_list = [0, 1]; length = 2; this_player = 2
    palyer_score_list = [0] * player_count
    while this_marble <= last_marble:
        if this_marble % 23 == 0:
            palyer_score_list[this_player] += this_marble
            offset = 7 if 7 < length else 7 % length
            if this_index >= offset:
                this_index -= offset
            else:
                this_index = length - (offset - this_index)
            palyer_score_list[this_player] += marble_list[this_index]
            marble_list.remove(marble_list[this_index])
            length -= 1
        else:
            this_index += 2
            if this_index == length:
                this_index = length
            elif this_index == length + 1:
                this_index = 1
            marble_list.insert(this_index, this_marble)
            length += 1
        this_marble += 1
        this_player = (this_player + 1) % player_count
    print(max(palyer_score_list))


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    # solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()