from typing import List


class Solution:

    def search(self, nums, left, right):
        if right - left == 1:
            if nums[right] < nums[left]:
                return nums[right]
            else:
                return nums[left]

        mid = int((left + right) / 2)
        if nums[right] < nums[left] < nums[mid]:
            return self.search(nums, mid, right)

        if nums[mid] < nums[right] < nums[left]:
            return self.search(nums, left, mid)

        if nums[left] < nums[mid] < nums[right]:
            return self.search(nums, left, mid)

    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.search(nums, 0, len(nums) - 1)