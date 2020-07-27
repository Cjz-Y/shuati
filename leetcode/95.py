from typing import List

from leetcode.TreeNode import TreeNode


class Solution:

    def dfs(self, start, end):

        if start > end:
            return [None]

        result = []
        for i in range(start, end + 1):
            lefts = self.dfs(start, i - 1)
            rights = self.dfs(i + 1, end)

            for left in lefts:
                for right in rights:
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    result.append(node)

        return result



    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.dfs(1, n) if n != 0 else []