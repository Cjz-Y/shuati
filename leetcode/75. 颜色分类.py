from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1
        index = 0
        while index <= right:
            if nums[index] == 1:
                index += 1
            elif nums[index] == 0:
                while nums[left] == 0 and left != index:
                    left += 1
                if left == index:
                    index += 1
                else:
                    nums[left], nums[index] = nums[index], nums[left]
                left += 1
            elif nums[index] == 2:
                while nums[right] == 2 and right != index:
                    right -= 1
                if right > index:
                    nums[right], nums[index] = nums[index], nums[right]
                right -= 1