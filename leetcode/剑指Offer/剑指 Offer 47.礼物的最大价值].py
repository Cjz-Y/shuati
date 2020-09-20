from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:


        f = [[0] * len(i) for i in grid]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                temp = 0
                if i > 0:
                    temp = max(temp, f[i - 1][j])
                if j > 0:
                    temp = max(temp, f[i][j - 1])

                f[i][j] = temp + grid[i][j]

        return f[len(grid) - 1][len(grid[0]) - 1]