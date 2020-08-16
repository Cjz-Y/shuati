# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from leetcode.TreeNode import TreeNode


class Solution:

    def back(self, preorder, pre_begin, pre_end, inorder, in_begin, in_end):
        node = TreeNode(preorder[pre_begin])
        if self.pos_in[preorder[pre_begin]] != in_begin:
            left = self.back(preorder, pre_begin + 1, pre_begin + self.pos_in[preorder[pre_begin]] - in_begin,
                             inorder, in_begin, self.pos_in[preorder[pre_begin]] - 1)
            node.left = left
        if self.pos_in[preorder[pre_begin]] != in_end:
            right = self.back(preorder, pre_begin + self.pos_in[preorder[pre_begin]] - in_begin + 1, pre_end,
                              inorder, self.pos_in[preorder[pre_begin]] + 1, in_end)
            node.right = right
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        self.pos_pre = {}
        self.pos_in = {}
        for i in range(len(preorder)):
            self.pos_pre[preorder[i]] = i
        for i in range(len(inorder)):
            self.pos_in[inorder[i]] = i

        return self.back(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

