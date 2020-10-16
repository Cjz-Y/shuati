# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from leetcode.TreeNode import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        def back(result, node, s):
            if not node.left and not node.right and s == sum:
                ans.append(result.copy())
                return

            if node.left:
                result.append(node.left.val)
                back(result, node.left, s + node.left.val)
                result.pop()

            if node.right:
                result.append(node.right.val)
                back(result, node.right, s + node.right.val)
                result.pop()

        back([root.val], root, root.val)
        return ans
