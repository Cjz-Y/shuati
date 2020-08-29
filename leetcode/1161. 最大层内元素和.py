from leetcode.TreeNode import TreeNode


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        ans_value  = -999999
        ans = -1

        current = [root]
        floor = 1
        while current:
            next = []
            sum = 0
            for node in current:
                sum += node.val
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            if sum > ans_value:
                ans_value = sum
                ans = floor
            floor += 1
            current = next

        return ans

