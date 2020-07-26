from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        f = [[0] * len(obstacleGrid[i]) for i in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 0:
            f[0][0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 0:
                    if i > 0:
                        f[i][j] += f[i - 1][j]
                    if j > 0:
                        f[i][j] += f[i][j - 1]

        return f[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]