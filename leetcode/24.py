from leetcode.ListNode import ListNode


class Solution:

    def back(self, root, swap):
        if not root.next:
            return root

        next = self.back(root.next, not swap)

        if swap:
            next_next = next.next
            next.next = root
            root.next = next_next
            return next
        else:
            root.next = next
            return root

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self.back(head, True)