from typing import List


class Solution:

    def rejust(self, nums, target):
        left = 2 * target + 1
        right = 2 * target + 2
        temp = target
        if left < len(nums) and nums[left] > nums[temp]:
            temp = left
        if right < len(nums) and nums[right] > nums[temp]:
            temp = right

        if temp != target:
            nums[temp], nums[target] = nums[target], nums[temp]
            self.rejust(nums, temp)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(int(len(nums) / 2), -1, -1):
            self.rejust(nums, i)

        # print(nums)

        for i in range(k - 1):
            nums[0], nums[len(nums) - 1] = nums[len(nums) - 1], nums[0]
            nums.pop()
            self.rejust(nums, 0)

        return nums[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    solution = Solution()
    print(solution.findKthLargest(nums, k))