from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_null = -99999
        max_null = 99999

        f = [min_null for i in range(len(nums))]
        g = [max_null for i in range(len(nums))]

        ans = min_null
        f[0] = nums[0]
        g[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max([f[i - 1] * nums[i], g[i - 1] * nums[i], nums[i]])
            g[i] = min([f[i - 1] * nums[i], g[i - 1] * nums[i], nums[i]])
            ans = max(ans, f[i])
        return ans