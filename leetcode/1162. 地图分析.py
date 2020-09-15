from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        null = 99999


        dist = [[null] * len(grid[i]) for i in range(len(grid))]
        process = [(1,0), (0, 1), (-1, 0), (0, -1)]
        current = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dist[i][j] = null
                else:
                    dist[i][j] = 0
                    current.append((i, j))

        ans = -1
        ans_x = -1
        ans_y = -1
        while current:
            next = []
            for (x, y) in current:

                for (process_x, process_y) in process:
                    xx = x + process_x
                    yy = y + process_y
                    if 0 <= xx < len(grid) and 0 <= yy < len(grid[xx]):
                        if dist[x][y] + 1 < dist[xx][yy]:
                            next.append((xx, yy))
                            dist[xx][yy] = dist[x][y] + 1
                            if dist[xx][yy] > ans:
                                ans = dist[xx][yy]
                                ans_x = xx
                                ans_y = yy

            current = next

        return ans


