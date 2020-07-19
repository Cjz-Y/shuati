from leetcode.ListNode import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 获取长度
        length = 0
        index = head
        while index:
            index = index.next
            length = length + 1
        mid = int(length / 2)
        # print('length = %d' % length)

        # 获取中间节点
        index = head
        mid_index = 0
        while index:
            mid_index = mid_index + 1
            if mid_index == mid:
                break
            index = index.next

        # print('mid_index = %d' % index.val)
        # 截断变成两节
        right = index.next
        index.next = None

        # 反转后节
        current = None
        next = right
        while next:
            next_next = next.next
            next.next = current
            current = next
            next = next_next

        # 合共两节
        new_head = ListNode(0)
        index = new_head
        while current or head:
            if head:
                index.next = head
                index = index.next
                head = head.next
            if current:
                index.next = current
                index = index.next
                current = current.next

        print('ok')

if __name__ == '__main__':
    solution = Solution()
    one = ListNode(1)
    # two = ListNode(2)
    # thr = ListNode(3)
    # fou = ListNode(4)
    #
    # one.next = two
    # two.next = thr
    # thr.next = fou

    print(solution.reorderList(one))