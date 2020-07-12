# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from leetcode.TreeNode import TreeNode

class Solution:
    ans = -999999

    def f(self, root:TreeNode):

        max_value = root.val
        if root.right is not None:
            right = self.f(root.right)
            max_value = max(max_value, root.val + right)

        if root.left is not None:
            left = self.f(root.left)
            max_value = max(max_value, root.val + left)

        self.ans = max(self.ans, max_value)
        if root.right is not None and root.left is not None:
            self.ans = max(self.ans, root.val + right + left)

        return max_value


    def maxPathSum(self, root: TreeNode) -> int:

        self.f(root)
        return self.ans

