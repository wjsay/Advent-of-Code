

def read_txt(filename):
    data = []
    with open(filename, 'r') as fin:
        for line in fin.readlines():
            data.append(line.strip('\n'))
    return data


def work(state):
    pos = state.rfind('#')
    if pos != -1:
        state += '.' * (5 - (len(state) - pos - 1))
    pos = state.find('#')
    if pos != -1:
        state = ('.' * (5 - pos)) + state
    return state


def solution1(data, gen=20):
    state = data[0].strip('initial state: ')
    left = 0
    rule_set = set()
    for rule in data[2:]:
        if rule[-1] == '#':
            rule_set.add(rule[0:5])
    for year in range(1, gen + 1):
        state = work(state)
        new_state = str('')
        for idx in range(0, len(state) - 5):
            if state[idx:idx+5] in rule_set:
                new_state += '#'
            else:
                new_state += '.'
        left += new_state.find('#') - (5 - 2)
        state = new_state
    count = 0
    state = state[state.find('#'):]
    for idx, ch in enumerate(list(state), left):
        if ch == '#':
            count += idx
    print(count)


def solution2(data, gen):
    state = data[0].strip('initial state: ')
    left = 0
    rule_set = set()
    for rule in data[2:]:
        if rule[-1] == '#':
            rule_set.add(rule[0:5])
    for year in range(1, gen + 1):
        state = work(state)
        new_state = str('')
        for idx in range(0, len(state) - 5):
            if state[idx:idx+5] in rule_set:
                new_state += '#'
            else:
                new_state += '.'
        if state == work(new_state):
            # print('----', year)  # 126 年后不再变化
            break
        left += new_state.find('#') - (5 - 2)
        state = new_state
    count = 0
    state = state[state.find('#'):]
    for idx, ch in enumerate(list(state), left):
        if ch == '#':
            count += idx + (gen - year)
    print(count)


def main():
    filename = 'input.txt'
    data = read_txt(filename)
    solution1(data)
    # solution2(data, 50000000000)


if __name__ == '__main__':
    main()
