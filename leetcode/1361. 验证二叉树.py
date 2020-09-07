from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        in_degree = [0 for i in range(n)]

        for child in leftChild:
            if child != -1:
                in_degree[child] += 1

        for child in rightChild:
            if child != -1:
                in_degree[child] += 1

        root = -1
        for node in range(n):
            if in_degree[node] == 0:
                if root == -1:
                    root = node
                else:
                    return False
            if in_degree[node] > 1:
                return False
        if root == -1:
            return False

        find = set()
        find.add(root)

        def dfs(node):
            if leftChild[node] != -1 and leftChild[node] not in find:
                find.add(leftChild[node])
                dfs(leftChild[node])
            if rightChild[node] != -1 and rightChild[node] not in find:
                find.add(rightChild[node])
                dfs(rightChild[node])

        dfs(root)

        return len(find) == n


