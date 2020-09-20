# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

from leetcode.ListNode import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        def back(node):
            if node.next:
                back(node.next)

            ans.append(node.val)


        ans = []
        if head:
            back(head)

        return ans
