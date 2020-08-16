from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def search(left, right):
            if left == right:
                return left

            mid = int((left + right) / 2)
            if nums[mid] > nums[mid + 1]:
                return search(left, mid)
            else:
                return search(mid + 1, right)

        return search(0, len(nums) - 1)