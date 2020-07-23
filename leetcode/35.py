from typing import List


class Solution:


    def search(self, num, left, right, target):
        mid = int((left + right) / 2)
        if target == num[mid]:
            return mid

        if left == right and target > num[mid]:
            return left + 1
        elif left == right and target < num[mid]:
            return left

        if target > num[mid]:
            return self.search(num, mid + 1, right, target)
        else:
            return self.search(num, left, mid, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.search(nums, 0, len(nums) - 1, target)