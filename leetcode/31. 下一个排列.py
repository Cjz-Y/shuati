from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        if index != -1:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[index]:
                    nums[index], nums[i] = nums[i], nums[index]
                    break

        start = index + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1