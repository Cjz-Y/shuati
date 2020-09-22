# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.TreeNode import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        print(A.val, B.val)
        if not A or not B:
            return False

        def compare(a, b):
            if not b:
                return True
            if not a:
                return False
            if a.val != b.val:
                return False
            return compare(a.left, b.left) and compare(a.right, b.right)

        result = compare(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        print(result)
        return result