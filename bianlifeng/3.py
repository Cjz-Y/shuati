root = input()
n = int(input())

child = {}


for i in range(n):
    line = input()
    index = line.find('->')
    node = line[:index]
    point = line[index + 2:]

    temp_list = child.get(node, [])
    temp_list.append(point)
    child[node] = temp_list


use = set()
ans = []

def search(x):
    childs = child.get(x, [])
    for i in range(len(childs)):
        if childs[i] not in use:
            ans.append(childs[i])
            use.add(childs[i])
            search(childs[i])

use.add(root)
search(root)
print(len(ans))


