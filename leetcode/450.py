from leetcode.TreeNode import TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key == root.val:
            if not root.right and not root.left:
                return None
            if root.right:
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, root.val)
                return root
            if not root.right and root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                root.val = predecessor.val
                root.left = self.deleteNode(root.left, root.val)
                return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root






    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val != key:
            if root.left:
                left = self.deleteNode(root.left, key)
                root.left = left
            if root.right:
                right = self.deleteNode(root.right, key)
                root.right = right
            return root

        else:
            if root.left:
                left = root.left

                if left and not left.left and left.right:
                    left_right = left.right
                    left.right = self.deleteNode(left_right, left_right.val)
                    left_right.left = left
                    left_right.right = root.right
                    return left_right


                real_left = self.deleteNode(root.left, root.left.val)
                right = root.right
                left.left = real_left
                left.right = right
                return left

            if root.right:
                return root.right

            return None