from leetcode import ListNode


class Solution:

    def reverse(self, current):
        print(current.val)

        if current.next:
            next = self.reverse(current.next)
            next.next = current

        return current



    def reverseList(self, head: ListNode) -> ListNode:
        tail = head
        while tail and tail.next:
            tail = tail.next
        self.reverse(head)
        head.next = None
        return tail


if __name__ == '__main__':
    solution = Solution()

    one = ListNode.ListNode(1)
    two = ListNode.ListNode(2)
    thr = ListNode.ListNode(3)
    fou = ListNode.ListNode(4)
    fiv = ListNode.ListNode(5)

    one.next = two
    two.next = thr
    thr.next = fou
    fou.next = fiv

    print(solution.reverseList(one).val)
