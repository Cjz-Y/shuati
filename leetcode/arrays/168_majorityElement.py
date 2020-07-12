from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        time = 0
        index = 0
        for num in nums:
            if time == 0:
                index = num
                time = 1
            elif num == index:
                time += 1
            elif num != index:
                time -= 1

        return index