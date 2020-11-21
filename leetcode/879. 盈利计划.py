from typing import List
import math


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        mod = 10 ** 9 + 7
        f = [[0 for i in range(P + 1)] for j in range(G + 1)]

        f[0][0] = 1

        for index in range(len(profit)):
            for i in range(G, -1, -1):
                for j in range(P, -1, -1):
                    if i + group[index] <= G:
                        max_profile = min(P, j + profit[index])
                        f[i + group[index]][max_profile] = (f[i + group[index]][max_profile] + f[i][j]) % mod

        ans = 0
        for i in range(G + 1):
            ans = (ans + f[i][P]) % mod
        return ans