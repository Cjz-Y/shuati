from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        def find(x):
            while father[x] != x:
                father[x] = father[father[x]]
                x = father[x]

            return x

        father = [i for i in range(len(s))]
        child = {}

        for pair in pairs:
            father1 = find(pair[0])
            father2 = find(pair[1])
            if father1 != father2:
                root_child = child.get(father1, [])
                child_child = child.get(father2, [])
                child_child.append(father2)
                root_child.extend(child_child)
                child[father1] = root_child
                if father2 in child:
                    child.pop(father2)

                father[father2] = father1

        print(child)
        ans = list(s)

        for item, childs in child.items():
            childs.append(item)
            childs.sort()

            string = []
            for child_index in childs:
                string.append(s[child_index])
            string.sort()

            for i in range(len(string)):
                ans[childs[i]] = string[i]

        return ''.join(ans)