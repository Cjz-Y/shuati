from typing import List
import heapq

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        item_x = [1, 0, -1, 0]
        item_y = [0, 1, 0, -1]

        heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(heap, (matrix[i][j], (i, j)))

        f = [[1] * len(matrix[i]) for i in range(len(matrix))]

        ans = 1

        while heap:
            item, (x, y) = heapq.heappop(heap)

            for i in range(4):
                xx = x + item_x[i]
                yy = y + item_y[i]
                if 0 <= xx < len(matrix) and 0 <= yy < len(matrix[xx]) and item < matrix[xx][yy]:
                    f[xx][yy] = max(f[xx][yy], f[x][y] + 1)
                    ans = max(ans, f[xx][yy])

        return ans



