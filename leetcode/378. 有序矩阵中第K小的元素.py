import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(mid):
            i, j = len(matrix) - 1, 0
            num = 0

            while i >= 0 and j < len(matrix[i]):
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1

            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left



    def _kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        小根堆写法，时间复杂度是O(klogk)，如果k=n2时，算法的复杂度退化到O(n2logn)
        :param matrix:
        :param k:
        :return:
        """

        index = 0
        heap = []
        find = set()
        find.add((0,0))
        heapq.heappush(heap, (matrix[0][0], (0,0)))
        while index != k - 1:
            (value, (x, y)) = heapq.heappop(heap)
            if x + 1 < len(matrix) and (x+1, y) not in find:
                find.add((x+1, y))
                heapq.heappush(heap, (matrix[x+1][y], (x+1, y)))
            if y + 1 < len(matrix[x]) and (x, y+1) not in find:
                find.add((x, y+1))
                heapq.heappush(heap, (matrix[x][y+1], (x, y+1)))
            index += 1

        ans, (x, y) = heapq.heappop(heap)
        return ans