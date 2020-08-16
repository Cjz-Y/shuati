# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from leetcode.TreeNode import TreeNode


class Solution:

    def back(self, inorder, in_begin, in_end, postorder, post_begin, post_end):
        node = TreeNode(postorder[post_end])
        if self.pos_in[node.val] != in_begin:
            left = self.back(inorder, in_begin, self.pos_in[node.val] - 1,
                             postorder, post_begin, post_begin + self.pos_in[node.val] - in_begin - 1)
            node.left = left
        if self.pos_in[node.val] != in_end:
            right = self.back(inorder, self.pos_in[node.val] + 1, in_end,
                              postorder, post_begin + self.pos_in[node.val] - in_begin, post_end - 1)
            node.right = right
        return node



    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder and not inorder:
            return None
        self.pos_post = {}
        self.pos_in = {}
        for i in range(len(postorder)):
            self.pos_post[postorder[i]] = i
        for i in range(len(inorder)):
            self.pos_in[inorder[i]] = i

        return self.back(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)