from leetcode.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

            if not fast or not slow:
                return False

            if slow == fast:
                return True