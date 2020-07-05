from leetcode.TreeNode import TreeNode

class Solution:

    balance = True

    def find_deep(self, current_node):
        if current_node == None:
            return 0
        left_depth = self.find_deep(current_node.left)
        right_depth = self.find_deep(current_node.right)

        if not self.balance:
            return

        if left_depth - right_depth > 1 or left_depth - right_depth < -1:
            self.balance = False

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


    def isBalanced(self, root: TreeNode) -> bool:
        self.find_deep(root)
        return self.balance