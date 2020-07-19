from typing import List

from leetcode.TreeNode import TreeNode


class Solution:
    # 中序遍历的时候，不断往左遍历遍历完了先加上根节点然后跳到右节点继续往左
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []

        current = root
        while current or len(stack) != 0:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result