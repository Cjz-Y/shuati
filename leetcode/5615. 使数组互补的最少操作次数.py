from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        f = [0 for i in range(2 * limit + 2)]
        for i in range(len(nums) // 2):
            a = nums[i]
            b = nums[-i - 1]
            left_index = 1 + min(a, b)
            right_index = limit + max(a, b)
            # 2 - left - a + b - right - 2 * limit
            f[2] += 2
            f[left_index] -= 1
            f[right_index + 1] += 1
            f[2 * limit + 1] -= 2
            f[a + b] -= 1
            f[a + b + 1] += 1

        ans = 99999999
        sum_temp = 0
        for i in range(2, 2 * limit + 1):
            sum_temp += f[i]
            ans = min(ans, sum_temp)
        return ans


