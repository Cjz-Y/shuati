from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        null = 0
        n = len(nums)
        f = [[null] * (n + 1) for i in range(n + 1)]

        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                for mid in range(start, end + 1):
                    if start == 0:
                        left = 1
                    else:
                        left = nums[start - 1]
                    if end == n - 1:
                        right = 1
                    else:
                        right = nums[end + 1]
                    f[start][end] = max(f[start][end], left * nums[mid] * right + f[start][mid - 1] + f[mid + 1][end])

        return f[0][n - 1]