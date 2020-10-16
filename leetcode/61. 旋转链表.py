# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.ListNode import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return None

        node = head
        length = 1
        while node.next:
            node = node.next
            length += 1

        if k > length:
            k = k % length

        if k == 0:
            return head
        else:
            node.next = head

            k = length - k
            temp = 1
            node = head
            while temp != k:
                node = node.next
                temp += 1
            ans = node.next
            node.next = None

            return ans
