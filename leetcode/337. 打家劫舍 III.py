# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.TreeNode import TreeNode


class Solution:
    def back(self, root):
        if not root:
            return 0, 0

        rob_left, no_rob_left = self.back(root.left)
        rob_right, no_rob_right = self.back(root.right)

        rob = no_rob_left + no_rob_right + root.val
        left_max = max(rob_left, no_rob_left)
        right_max = max(rob_right, no_rob_right)
        no_rob = left_max + right_max

        return rob, no_rob

    def rob(self, root: TreeNode) -> int:
        rob, no_rob = self.back(root)
        return max(rob, no_rob)



    ans = 0
    null = 0

    def back(self, root: TreeNode):
        if not root.right and not root.left:
            root.val = max(root.val, self.null)
            return

        if root.left:
            self.back(root.left)
        if root.right:
            self.back(root.right)

        temp = self.null

        left_son = self.null
        if root.left and root.left.left:
            left_son = max(left_son, left_son + root.left.left.val)
        if root.left and root.left.right:
            left_son = max(left_son, left_son + root.left.right.val)

        right_son = self.null
        if root.right and root.right.left:
            right_son = max(right_son, right_son + root.right.left.val)
        if root.right and root.right.right:
            right_son = max(right_son, right_son + root.right.right.val)


        # 1.l+r 2. l 3. r
        if root.left or root.right:
            if root.left:
                temp = max(temp, root.left.val)
            if root.right:
                temp = max(temp, root.right.val)
            if root.left and root.right:
                temp = max(temp, root.left.val + root.right.val)

        if root.left and right_son != self.null:
            temp = max(temp, root.left.val + right_son)
        if root.right and left_son != self.null:
            temp = max(temp, root.right.val + left_son)

        if left_son != self.null or right_son != self.null:
            temp = max(temp, left_son + right_son + root.val)

        root.val = temp
        if temp > self.ans:
            self.ans = temp


    def rob2(self, root: TreeNode) -> int:
        self.ans = self.null
        self.back(root)
        return self.ans