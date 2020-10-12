# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from leetcode.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:

        ans = []

        if not root:
            return ans

        cur = [root]
        while cur:
            next = []
            for node in cur:
                ans.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            cur = next
        return ans