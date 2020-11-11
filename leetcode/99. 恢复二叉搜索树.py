# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from leetcode.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        last, now = None, None
        ans = []
        cur = root
        while cur:
            # 当前节点的做儿子为空
            if not cur.left:
                last = now
                now = cur
                if last and last.val > now.val:
                    ans.append(last)
                    ans.append(now)

                cur = cur.right
            # 当前节点的左儿子不为空
            else:
                # 搜索当前节点的前驱节点
                precursor = cur.left
                while precursor.right and precursor.right != cur:
                    precursor = precursor.right

                # 如果前驱节点的右孩子为空，就把右孩子指向当前节点
                if not precursor.right:
                    precursor.right = cur
                    cur = cur.left

                # 如果前驱节点的右孩子 == 当前节点，那么将他右孩子设为空，输出当前节点，把当前节点更新为右孩子
                elif precursor.right == cur:
                    precursor.right = None
                    last = now
                    now = cur
                    if last and last.val > now.val:
                        ans.append(last)
                        ans.append(now)
                    cur = cur.right
        # print(ans)
        if len(ans) == 2:
            ans[0].val, ans[1].val = ans[1].val, ans[0].val
        else:
            ans[0].val, ans[-1].val = ans[-1].val, ans[0].val

