from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp_time = 0
        index = 0
        while index < len(nums):
            if index == 0 or nums[index] != nums[index - 1]:
                temp_time = 1
                index += 1
            else:
                if temp_time == 2:
                    nums.pop(index)
                else:
                    temp_time += 1
                    index += 1
        return len(nums)
