from leetcode.TreeNode import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val != q.val:
                return False
            else:
                flag = True
                if p.left and q.left:
                    flag = self.isSameTree(p.left, q.left)
                elif not p.left and not q.left:
                    pass
                else:
                    return False

                if not flag:
                    return flag

                if p.right and q.right:
                    return self.isSameTree(p.right, q.right)
                elif not p.right and not q.right:
                    return True
                else:
                    return False
        elif not p and not q:
            return True
        else:
            return False

