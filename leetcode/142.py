from leetcode.ListNode import ListNode


class Solution:


    def detectCycle2(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while True:
            if not fast or not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        result = head
        while result != slow:
            result = result.next
            slow = slow.next
        return result

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        found = set()

        while head:

            found.add(head)
            # print(head.val)
            # print(found)
            if head.next and head.next in found:
                    return head.next
            head = head.next

        return None


if __name__ == '__main__':
    solution = Solution()
    one = ListNode(1)
    two = ListNode(2)
    thr = ListNode(3)
    fou = ListNode(4)

    one.next = two
    two.next = thr
    thr.next = fou
    fou.next = two

    print(solution.detectCycle(one))