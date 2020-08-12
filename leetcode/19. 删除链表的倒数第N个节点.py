# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        num = 0

        vir_head = ListNode(0)
        vir_head.next = head

        temp = vir_head
        real_temp = vir_head
        while temp.next:
            num += 1
            temp = temp.next

            if num > n:
                real_temp = real_temp.next


        if real_temp.next == head:
            return head.next
        else:
            real_temp.next = real_temp.next.next
            return head
