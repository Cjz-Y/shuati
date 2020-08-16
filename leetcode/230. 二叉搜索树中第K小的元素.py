# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        time = 1

        stack = []

        while True:
            # 递归左子树
            while root:
                stack.append(root)
                root = root.left

            if time == k:
                return stack.pop().val
            else:
                # 弹出中间
                root = stack.pop()
                # 递归右子树的左子树
                root = root.right
                time += 1

