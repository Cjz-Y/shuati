from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        null = -99999
        f = [null for i in range(len(prices))]
        g = [null for i in range(len(prices))]

        f[0] = -prices[0] - fee
        g[0] = 0

        for i in range(1, len(prices)):
            f[i] = max(f[i - 1], g[i - 1] - prices[i] - fee)
            g[i] = max(g[i - 1], f[i - 1] + prices[i])

        return g[len(prices) - 1]