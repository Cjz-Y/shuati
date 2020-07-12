from typing import List

from leetcode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        current = []
        if root is not None:
            current.append(root)

        need_reverse = False
        while len(current) != 0:
            current_value = []
            next = []
            for node in current:
                current_value.append(node.val)

                if need_reverse:
                    if node.left is not None:
                        next.insert(0, node.left)
                    if node.right is not None:
                        next.insert(0, node.right)
                else:
                    if node.right is not None:
                        next.insert(0, node.right)
                    if node.left is not None:
                        next.insert(0, node.left)

            ans.append(current_value)
            current = next
            need_reverse = not need_reverse

        return ans