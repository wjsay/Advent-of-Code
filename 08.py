

def read_txt(filename):
    with open(filename, 'r') as fin:
        data = [i for i in map(int, fin.readline().strip('\n').split())]
        return data


def solution1(data_list):
    all_metadata_list = []
    stack = [{
        'child_count': data_list[0],
        'meta_count': data_list[1],
    }]
    this_index = 2
    while this_index < len(data_list):
        if stack[-1]['child_count'] != 0:
            stack[-1]['child_count'] -= 1
            stack.append({
                'child_count': data_list[this_index],
                'meta_count': data_list[this_index + 1],
            })
            this_index += 2
        if stack[-1]['child_count'] == 0:
            all_metadata_list.append(data_list[this_index: this_index + stack[-1]['meta_count']])
            this_index += stack[-1]['meta_count']
            stack.pop()
    count = 0
    for metadata_list in all_metadata_list:
        count += sum(metadata_list)
    print(count)


def solution2(data_list):
    stack = [{
        'child_count': data_list[0],
        'meta_count': data_list[1],
        'parent_index': -1,
        'children_index': [],
        'metadata': [],
        'this_index': 0,
    }]
    all_node_list = []
    index_map = {0: 0, }
    this_index = 2; order = 1
    while this_index < len(data_list):
        if stack[-1]['child_count'] != 0:
            stack[-1]['child_count'] -= 1
            stack[-1]['children_index'].append(this_index)
            stack.append({
                'child_count': data_list[this_index],
                'meta_count': data_list[this_index + 1],
                'parent_index': stack[-1]['this_index'],
                'children_index': [],
                'metadata': [],
                'this_index': this_index,
            })
            index_map[this_index] = order
            order += 1
            this_index += 2
        if stack[-1]['child_count'] == 0:
            stack[-1]['metadata'] = data_list[this_index: this_index + stack[-1]['meta_count']]
            stack[-1]['child_count'] = len(stack[-1]['children_index'])
            all_node_list.append(stack[-1])
            this_index += stack[-1]['meta_count']
            stack.pop()
    all_node_list.sort(key=lambda item: item['this_index'])
    result = 0
    stack = [all_node_list[index_map[0]]]
    while stack:
        node = stack.pop()
        if node['child_count'] == 0:
            result += sum(node['metadata'])
        else:
            for metadata in node['metadata']:
                if metadata <= node['child_count']:
                    stack.append(all_node_list[index_map[node['children_index'][metadata-1]]])
    print(result)
    # for node in all_node_list:
    #     print(node)
    # print(index_map)

# {'child_count': 2, 'meta_count': 3, 'parent_index': -1, 'children_index': [2, 7], 'metadata': [1, 1, 2], 'this_index': 0}
# {'child_count': 0, 'meta_count': 3, 'parent_index': 0, 'children_index': [], 'metadata': [10, 11, 12], 'this_index': 2}
# {'child_count': 1, 'meta_count': 1, 'parent_index': 0, 'children_index': [9], 'metadata': [2], 'this_index': 7}
# {'child_count': 0, 'meta_count': 1, 'parent_index': 7, 'children_index': [], 'metadata': [99], 'this_index': 9}
# {0: 0, 2: 1, 7: 2, 9: 3}


def main():
    file_name = 'input.txt'
    data = read_txt(file_name)
    # solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
