from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        ans = 0
        time = {}
        for num in nums:
            if (k - num) in time and time[k - num] > 0:
                time[k - num] -= 1
                ans += 1
            else:
                time[num] = time.get(num, 0) + 1
        return ans
