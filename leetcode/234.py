from leetcode.ListNode import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        length = 0
        index = head
        while index:
            length = length + 1
            index = index.next

        mid_index = int(length / 2)

        mid = 0
        index = head
        while index:
            mid = mid + 1
            if mid == mid_index:
                break
            index = index.next

        if length % 2 == 0:
            right = index.next
        else:
            right = index.next.next
        index.next = None

        # 旋转后面一节
        current = None
        next = right
        while next:
            next_item = next.next
            next.next = current
            current = next
            next = next_item

        while current and head:
            if current.val == head.val:
                current = current.next
                head = head.next
            else:
                return False
        return True



