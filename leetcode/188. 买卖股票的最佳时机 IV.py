from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        null = -999999
        n = 2 * k
        f = [null for i in range(n)]

        f[0] = -prices[0]
        ans = 0

        for i in range(1, len(prices)):

            for j in range(len(f)):
                if j % 2 == 0:
                    if j == 0:
                        f[j] = max([f[j], -prices[i]])
                    else:
                        f[j] = max([f[j], f[j - 1] - prices[i]])
                else:
                    f[j] = max([f[j], f[j - 1] + prices[i]])
                if i == len(prices) - 1:
                    ans = max([ans, f[j]])

        return ans
