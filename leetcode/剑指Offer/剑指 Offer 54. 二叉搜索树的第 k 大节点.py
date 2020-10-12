# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.TreeNode import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        def back(node):

            if node.left:
                back(node.left)
            ans.append(node.val)
            if node.right:
                back(node.right)


        ans = []

        back(root)

        return ans[-k]