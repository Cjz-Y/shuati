from leetcode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        while head and head.next and head.next.val == head.val:
            while head.next and head.next.val == head.val:
                if head.next.next:
                    head.next = head.next.next
                else:
                    break
            head = head.next

        current  = head

        while current:
            if current.next and current.next.next and current.next.val == current.next.next.val:
                spec = current.next.val
                next_item = current.next
                while next_item and next_item.val == spec:
                    next_item = next_item.next
                current.next = next_item

            current = current.next

        return head




        # ## get real head
        #

        #
        # while current:
        #     if current.next and current.next.val == current.val:
        #         while current.next and current.next.val == current.val:
        #             current.next = current.next.next


