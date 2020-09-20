from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        null = 99999
        min_value = [[null] * len(prices) for i in range(len(prices))]
        for length in range(1, len(prices)):
            for start in range(len(prices) - length + 1):
                end = start + length - 1
                min_value[start][end] = min(prices[start], min_value[start + 1][end])
        f = []

        for i in range(len(prices)):
            for j in range(i):
                f[i] = max(f[i], f[j] + prices[i] - min_value[j + 2][i - 1])
