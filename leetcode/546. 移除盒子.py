from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        dp = [[[0] * len(boxes) for j in range(len(boxes))] for i in range(len(boxes))]

        def cal(l, r, k):
            if l > r:
                return 0

            while l < r and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            if dp[l][r][k] != 0:
                return dp[l][r][k]

            dp[l][r][k] = cal(l, r - 1, 0) + (k + 1) ** 2

            for i in range(l, r):
                if boxes[i] != boxes[r]:
                    continue
                else:
                    dp[l][r][k] = max(dp[l][r][k], cal(l, i, k + 1) + cal(i + 1, r - 1, 0))

            return dp[l][r][k]

        return cal(0, len(boxes) - 1, 0)
