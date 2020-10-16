# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.ListNode import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse(node):
            if not node.next:
                return node
            next = reverse(node.next)

            next.next = node
            return node

        if k == 1:
            return head

        virtual_head = ListNode()
        virtual_head.next = head

        pre_head = virtual_head
        head = virtual_head.next

        while True:
            # print(head.val)
            if not head:
                break
            temp = head
            temp_num = 1
            while temp_num != k and temp.next:
                temp = temp.next
                temp_num += 1

            if temp_num < k:
                break
            else:
                # 记录尾部节点和after尾部节点
                tail = temp
                after_tail = temp.next

                tail.next = None
                reverse(head)

                # 将逆转之后的头节点跟前一个节点链接 尾节点跟后一个链接
                pre_head.next = tail
                head.next = after_tail

                # 记录新的头
                pre_head = head
                head = after_tail

        return virtual_head.next






