# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if not headA or not headB:
            return None

        a = headA
        b = headB

        lasta = None
        lastb = None

        while a != b:
            if not a.next:
                if not lasta:
                    lasta = a
                a = headB
            else:
                a = a.next

            if not b.next:
                if not lastb:
                    lastb = b
                b = headA
            else:
                b = b.next

            if lasta and lastb and lasta != lastb:
                return None

        return a