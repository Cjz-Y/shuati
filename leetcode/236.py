from leetcode import TreeNode


class Solution:
    tree = []
    depth = []

    def get_list(self, root: TreeNode, dep):
        self.tree.append(root)
        self.depth.append(dep)

        if root.left is not None:
            self.get_list(root.left, dep + 1)

        if root.right is not None:
            self.get_list(root.right, dep + 1)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.tree = []
        self.depth = []
        self.get_list(root, 0)

        p_index = -1
        q_index = -1
        for i in range(len(self.tree)):
            if self.tree[i].val == p.val:
                p_index = i
            if self.tree[i].val == q.val:
                q_index = i
            if p_index != -1 and q_index != -1:
                break

        while p_index != q_index:
            if self.depth[p_index] < self.depth[q_index]:
                old_dep = self.depth[q_index]
                while self.depth[q_index] >= old_dep:
                    q_index -= 1
            else:
                old_dep = self.depth[p_index]
                while self.depth[p_index] >= old_dep:
                    p_index -= 1

        return self.tree[p_index]