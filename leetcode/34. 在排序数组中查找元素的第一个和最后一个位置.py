from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def search_com(left, right, condition):
            if left == right:
                return left

            mid = int((left + right) / 2)

            if condition == 1:
                if nums[mid] >= target:
                    return search_com(left, mid, condition)
                else:
                    return search_com(mid + 1, right, condition)
            else:
                if nums[mid] > target:
                    return search_com(left, mid, condition)
                else:
                    return search_com(mid + 1, right, condition)

        start = search_com(0, len(nums) - 1, 1)
        if nums[start] != target:
            return [-1, -1]
        end = search_com(0, len(nums) - 1, 0)
        if nums[end] != target:
            end -= 1

        return [start, end]


