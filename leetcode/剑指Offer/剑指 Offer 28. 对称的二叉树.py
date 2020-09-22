# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def compare(left, right):
            if not left and not right:
                return True
            if not left and right:
                return False
            if not right and left:
                return False
            if left.val != right.val:
                return False

            return compare(left.left, right.right) and compare(left.right, right.left)

        return compare(root.left, root.right)