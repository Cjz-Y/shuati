from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0

        stack = []

        for i in range(len(height)):
            h = height[i]
            if h == 0:
                continue

            cal_height = 0
            while stack and stack[-1][0] <= h:
                ans += ((stack[-1][0] - cal_height) * (i - stack[-1][1] - 1))
                cal_height = stack[-1][0]
                stack.pop()

            if stack:
                ans += (h - cal_height) * (i - stack[-1][1] - 1)

            stack.append((h, i))
            print('i = %d, ans = %d, stack = %s' % (i, ans, stack))

        return ans

