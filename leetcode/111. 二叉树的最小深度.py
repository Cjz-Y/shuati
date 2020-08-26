from leetcode.TreeNode import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1