from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        value = []
        pos = []
        ans = 0
        for i in range(len(heights)):
            while len(value) != 0 and heights[i] < value[len(value) - 1]:
                heightest = value.pop()
                pos.pop()
                if len(pos) != 0:
                    length = (i - pos[len(pos) - 1] - 1)
                else:
                    length = i
                area = heightest * length
                ans = max(ans, area)
            value.append(heights[i])
            pos.append(i)

        return ans






