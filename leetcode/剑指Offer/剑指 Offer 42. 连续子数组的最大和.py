from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        null = -99999
        f = [null for i in range(len(nums))]
        f[0] = nums[0]
        ans = f[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1] + nums[i], nums[i])
            ans = max(ans, f[i])

        return ans