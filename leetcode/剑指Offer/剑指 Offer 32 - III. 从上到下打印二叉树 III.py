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
        reverse = False
        while cur:
            next = []
            ans_temp = []
            if not reverse:
                for i in range(len(cur) - 1, -1, -1):
                    node = cur[i]
                    ans_temp.append(node.val)
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
            else:
                for i in range(len(cur) - 1, -1 , -1):
                    node = cur[i]
                    ans_temp.append(node.val)
                    if node.right:
                        next.append(node.right)
                    if node.left:
                        next.append(node.left)
            ans.append(ans_temp)
            cur = next
            reverse = not reverse
        return ans
