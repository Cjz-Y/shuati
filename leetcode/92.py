from leetcode import ListNode


class Solution:
    new_head = None
    successor = None

    def reverse_node(self, root, n):
        if n == 0:
            self.successor = root.next
            self.new_head = root
            return root

        next = self.reverse_node(root.next, n - 1)
        next.next = root
        root.next = None
        return root

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            pre = None
            new_last = self.reverse_node(head, n - m)
        else:
            # 找到需要旋转的前一个节点
            index = 1
            pre = head
            while index != m - 1:
                index += 1
                pre = pre.next

            new_last = self.reverse_node(pre.next, n - m)
            # print('new_head = %d' % self.new_head.val)
            # print('new_last = %d' % new_last.val)
            pre.next = self.new_head

        new_last.next = self.successor

        return head if m != 1 else self.new_head

