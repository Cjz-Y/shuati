from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        null = -99999

        # 持有股票的最大收益
        f = [null for i in range(len(prices))]
        # 不持有股票 在冷却器
        g = [null for i in range(len(prices))]
        # 不持有股票 不在冷却器
        t = [null for i in range(len(prices))]

        f[0] = -prices[0]
        g[0] = 0
        t[0] = 0

        for i in range(1, len(prices)):
            f[i] = max(f[i - 1], t[i - 1] - prices[i])
            g[i] = max(f[i - 1] + prices[i])
            t[i] = max(t[i - 1], g[i - 1])

        return max(g[len(prices) - 1], t[len(prices) - 1])

