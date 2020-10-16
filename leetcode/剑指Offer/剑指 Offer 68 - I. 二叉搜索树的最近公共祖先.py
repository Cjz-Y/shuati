# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def back(node):

            if not node:
                return False

            left = back(node.left)
            right = back(node.right)

            if self.ans:
                return True


            if left and right:
                self.result = node
                self.ans = True
                return True

            if left and (node.val == p.val or node.val == q.val):
                self.result = node
                self.ans = True
                return True

            if right and (node.val == p.val or node.val == q.val):
                self.result = node
                self.ans = True
                return True

            return left or right or node.val == p.val or node.val == q.val

        self.ans = False
        self.result = None
        back(root)

        return self.result
