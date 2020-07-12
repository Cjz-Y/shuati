from leetcode import TreeNode


class Solution:

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        if val < root.val:
            root.left =  self.insertIntoBST(root.left, val)

        return root



    xl = []
    def bianli(self, node: TreeNode):
        if not node.right and not node.left:
            self.xl.append(node)
            return

        if not node.left:
            self.bianli(node.left)
        self.xl.append(node)
        if not node.right:
            self.bianli(node.right)

        return

    def insertIntoBST11(self, root: TreeNode, val: int) -> TreeNode:
        self.bianli(root)
        i = 0
        for i in range(len(self.xl)):
            if val > self.xl[i].val:
                break

        if not self.xl[i].right:
            self.xl[i].right = TreeNode(val)
            return root

        if not self.xl[i + 1].left:
            self.xl[i + 1].left = TreeNode(val)
            return root



