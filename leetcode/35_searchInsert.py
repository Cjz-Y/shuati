from typing import List


# 二分过程中是向下取整  所以当无法查找到时，mid必然==begin

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        begin = 0
        end = len(nums) - 1
        while True:
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                return mid
            elif mid == begin:
                return mid + 1
            elif target > nums[mid]:
                begin = mid
            elif target < nums[mid]:
                end = mid
