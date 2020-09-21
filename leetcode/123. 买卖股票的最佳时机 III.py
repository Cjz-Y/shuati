from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        null = -9999

        f = [null for i in range(len(prices))]
        g = [null for i in range(len(prices))]
        t = [null for i in range(len(prices))]
        e = [null for i in range(len(prices))]

        f[0] = -prices[0]
        g[0] = 0
        t[0] = null
        e[0] = null


        for i in range(1, len(prices)):
            f[i] = max(f[i - 1], -prices[i])
            g[i] = max(g[i - 1], f[i - 1] + prices[i])
            t[i] = max(t[i - 1], g[i - 1] - prices[i])
            e[i] = max(e[i - 1], t[i - 1] + prices[i])

        # print(f)
        # print(g)
        # print(t)
        # print(e)


        return max(e[len(prices) - 1], g[len(prices) - 1])


if __name__ == '__main__':
    p = [1,2,3,4,5]

    print(Solution().maxProfit(p))
