from leetcode.MapNode import MapNode as Node

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        stack = []          # 遍历栈
        found = set()       # 判断当前节点是否已经入栈了
        generate_map = {}   # 保存对应的clone值

        stack.append(node)
        found.add(node.val)
        while len(stack) != 0:
            current = stack.pop()

            clone_item = Node(current.val, [])
            generate_map[current.val] = clone_item

            for i in current.neighbors:
                if i.val not in found:
                    stack.append(i)
                    found.add(i.val)
                if i.val in generate_map.keys():
                    clone_item.neighbors.append(generate_map.get(i.val))
                    generate_map.get(i.val).neighbors.append(clone_item)

        return generate_map[1]

if __name__ == '__main__':
    one = Node(1, [])
    two = Node(2, [])
    thr = Node(3, [])
    fou = Node(4, [])

    one.neighbors.append(two)
    one.neighbors.append(thr)

    two.neighbors.append(one)
    two.neighbors.append(fou)

    thr.neighbors.append(one)
    thr.neighbors.append(fou)

    fou.neighbors.append(two)
    fou.neighbors.append(thr)

    solution = Solution()
    clone = solution.cloneGraph(one)

    print('ok')

