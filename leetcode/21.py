from leetcode.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l2:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        if not l1:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2