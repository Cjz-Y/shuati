from leetcode.ListNode import ListNode
from leetcode.TreeNode import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        def make_tree(node):
            if not node.next:
                return TreeNode(node.val)

            slow, fast, slow_slow = node, node, node
            while fast.next and fast.next.next:
                slow_slow = slow
                slow = slow.next
                fast = fast.next.next

            current = TreeNode(slow_slow.next.val)
            if slow_slow.next.next:
                right = make_tree(slow_slow.next.next)
                current.right = right
            slow_slow.next = None
            left = make_tree(node)
            current.left = left
            return current

        return make_tree(head)

