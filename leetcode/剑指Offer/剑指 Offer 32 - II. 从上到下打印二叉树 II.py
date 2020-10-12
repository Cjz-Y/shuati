# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from leetcode.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        ans = []
        if not root:
            return ans

        cur = [root]
        while cur:
            next = []
            ans_temp = []
            for node in cur:
                ans_temp.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            ans.append(ans_temp)
            cur = next
        return ans