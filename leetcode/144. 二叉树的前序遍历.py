# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from leetcode.TreeNode import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []


        ans = [root.val]
        stack = [root]

        while stack:

            while stack[-1].left:
                left_node = stack[-1].left
                if left_node:
                    stack.append(left_node)
                    ans.append(left_node.val)
                    stack[-2].left = None

            node = stack.pop()
            if node.right:
                ans.append(node.right.val)
                stack.append(node.right)
        return ans


