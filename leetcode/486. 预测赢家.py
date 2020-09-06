from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        f = [[] * len(nums) for i in range(len(nums))]

        for i in range(len(nums)):
            f[i][i] = nums[i]

        for length in range(2, len(nums) + 1):
            for start in range(len(nums) - length + 1):
                end = start + length - 1
                f[start][end] = max(nums[start] - f[start + 1][end], nums[end] - f[start][end - 1])

        return f[0][len(nums) - 1] > 0