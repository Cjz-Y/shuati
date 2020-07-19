from leetcode.ListNode import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        min_head = ListNode(0)
        max_head = ListNode(0)

        min_tail = min_head
        max_tail = max_head

        index = head
        while index:
            if index.val >= x:
                max_tail.next = ListNode(index.val)
                max_tail = max_tail.next
            else:
                min_tail.next = ListNode(index.val)
                min_tail = min_tail.next

            index = index.next

        min_tail.next = max_head.next

        return min_head.next


