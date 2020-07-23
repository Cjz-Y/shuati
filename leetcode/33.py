from typing import List


class Solution:

    def s(self, nums, left, right, target):
        if right - left == 1:
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            return -1

        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid
        if nums[right] < nums[left] < nums[mid]:
            if nums[left] <= target <= nums[mid]:
                return self.s(nums, left, mid, target)
            else:
                return self.s(nums, mid, right, target)
        if nums[mid] < nums[right] < nums[left]:
            if nums[mid] <= target <= nums[right]:
                return self.s(nums, mid, right, target)
            else:
                return self.s(nums,left, mid, target)

        if nums[left] < nums[mid] < nums[right]:
            if nums[left] <= target <= nums[mid]:
                return self.s(nums, left, mid, target)
            else:
                return self.s(nums, mid, right, target)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        return self.s(nums, 0, len(nums) - 1, target)