from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) % 2 == 0:
            n = k
        else:
            n = 1

        for i in range(n):
            index = i
            now = nums[index]
            while True:
                advance_index = (index +k) % len(nums)
                advance = nums[advance_index]
                nums[advance_index] = now
                now = advance
                index = advance_index
                if index == i:
                    break

    def rotate2(self, nums: List[int], k: int) -> None:
        length = len(nums)
        for i in range(k):
            temp1 = nums[length - 1]
            for j in range(length):
                temp2 = nums[j]
                nums[j] = temp1
                temp1 = temp2

    def reverse(self, nums):
        for i in range(int(len(nums) / 2)):
            nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]

    def rotate3(self, nums: List[int], k: int) -> None:
        self.reverse(nums)
        nums[:k] = self.reverse(nums[:k])
        nums[k:] = self.reverse(nums[k:])

    def rotate(self, nums: List[int], k: int) -> None:
        def swap(l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k %= len(nums)
        swap(0, len(nums) - 1)
        swap(0, k - 1)
        swap(k, len(nums) - 1)









