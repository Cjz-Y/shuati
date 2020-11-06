from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()

        f = [0 for i in range(len(satisfaction))]
        for i in range(len(satisfaction) - 2, -1, -1):
            f[i] = satisfaction[i + 1] + f[i + 1]

        ans = 0

        index = 1
        for i in range(len(satisfaction)):
            if index * satisfaction[i] + f[i] >= 0:
                ans += index * satisfaction[i]
                index += 1
        return ans
