from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        f = [0 for i in range(n)]
        g = [[0] * n for i in range(n)]

        for road in roads:
            x, y = road[0], road[1]

            f[x] += 1
            f[y] += 1
            g[x][y] = 1
            g[y][x] = 1

        f.sort(reverse=True)

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, f[i] + f[j] - g[i][j])

        return ans