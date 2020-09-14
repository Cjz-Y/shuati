from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        f = []

        for i in range(len(prices)):
            for j in range(i):
                for k in range(j + 2, i - 1):
                    f[i] = max(f[i], f[j] + prices[i] - prices[k])