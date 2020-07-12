from leetcode import TreeNode


class Solution:
    vaild = False

    def find_max_min(self, root: TreeNode):
        if not root.right and not root.left:
            return root.val, root.val

        current_max,  current_min = root.val, root.val

        if root.left:
            max_value, min_value = self.find_max_min(root.left)
            if self.vaild or max_value >= root.val:
                self.vaild = True
                return 0, 0

            current_max = max(max_value, current_max)
            current_min = min(min_value, current_min)

        if root.right:
            max_value, min_value = self.find_max_min(root.right)
            if self.vaild or min_value <= root.val:
                self.vaild = True
                return 0, 0
            current_max = max(max_value, current_max)
            current_min = min(min_value, current_min)

        return current_max, current_min


    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return not self.vaild
        self.find_max_min(root)
        return not self.vaild