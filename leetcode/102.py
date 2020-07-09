from typing import List

from leetcode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        current = []
        if root is not None:
            current.append(root)

        while len(current) != 0:
            current_value = []
            next = []
            for node in current:
                current_value.append(node.val)
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)

            ans.append(current_value)
            current = next

        return ans

