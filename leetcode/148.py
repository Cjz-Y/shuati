from leetcode.ListNode import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # print('head = %d' % head.val)
        if not head.next:
            return head

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

        # 将左右分别排序
        left = self.sortList(head)
        right = self.sortList(right)
        # print('left = %d, left.next is %s, right  = %d, right.next is %s' % (left.val, left.next, right.val, right.next))

        # 合并
        temp = ListNode(0)
        current = temp
        while left or right:
            # print('current = %d, left is %s, right is %s' % (current.val, left, right))

            if left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
            else:
                if not left:
                    current.next = right
                    right = right.next
                else:
                    current.next = left
                    left = left.next
            current = current.next
        return temp.next

if __name__ == '__main__':
    solution = Solution()
    one = ListNode(4)
    two = ListNode(2)
    thr = ListNode(1)
    fou = ListNode(3)

    one.next = two
    two.next = thr
    thr.next = fou

    print(solution.sortList(one))


