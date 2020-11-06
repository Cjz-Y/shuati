# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.TreeNode import TreeNode


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        depths = {}
        depth = 0

        index = 0
        while index < len(S):
            while S[index] == '-':
                depth += 1
                index += 1
            start_index = index
            while index < len(S) and S[index] != '-':
                index += 1

            val = int(S[start_index: index])
            node = TreeNode(val)

            temp_list = depths.get(depth, [])
            temp_list.append(node)
            depths[depth] = temp_list

            # print(depth, depths)

            if depth != 0:
                father = depths[depth - 1][-1]
                if father.left:
                    father.right = node
                else:
                    father.left = node
            depth = 0

        return depths[0][0]


