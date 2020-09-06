from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = [1 for i in range(len(nums))]

        temp = 1
        for i in range(len(nums)):
            f[i] = temp
            temp *= nums[i]

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            f[i] *= temp
            temp *= nums[i]

        return f
