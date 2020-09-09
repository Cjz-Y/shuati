from typing import List

from leetcode.ListNode import ListNode
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def push(val, node):
            heap.append((val, node))
            pos = len(heap) - 1

            while pos >= 0:
                father = (pos - 1) >> 1
                parent_val, parent_node = heap[father]
                if parent_val > val:
                    heap[pos] = (parent_val, parent_node)
                    pos = father
                    continue
                break
            heap[pos] = (val, node)

        def pop():

            last_val, last_node = heap.pop()
            if heap:
                return_val, return_node = heap[0]

                pos = 0
                child = 2 * pos + 1
                while child < len(heap):
                    right_child = child + 1
                    if right_child < len(heap) and heap[right_child][0] < heap[child][0]:
                        child = right_child

                    if heap[child][0] < last_val:
                        heap[pos] = heap[child]
                        pos = child
                        child = 2 * pos + 1
                    else:
                        break

                heap[pos] = (last_val, last_node)

                return (return_val, return_node)

            return (last_val, last_node)

        heap = []

        for node in lists:
            heapq.heappush(heap, (node.val, node))

        head = ListNode()
        temp = head


        while heap:
            val, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            temp.next = node
            temp = temp.next
        return head.next

