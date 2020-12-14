# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.TreeNode import TreeNode


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def back(node):
            if not node:
                return None
            left = back(node.left)
            right = back(node.right)

            if not left and not right:
                if node.val == target:
                    return None

            node.left = left
            node.right = right
            return node

        return back(root)
