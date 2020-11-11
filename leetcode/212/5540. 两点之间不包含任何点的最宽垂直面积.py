from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        unique = set()
        for x, y in points:
            unique.add(x)
        unique = list(unique)
        unique.sort()

        ans = 0
        for i in range(1, len(unique)):
            ans = max(ans, unique[i] - unique[i - 1])
        return ans