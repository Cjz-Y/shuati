from typing import List

# 给定数组 nums = [1,1,2],
#
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
#
# 数组是排序的  需要考虑的排序数组的特点


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        q = 1
        while (q < len(nums)):
            if (nums[p] != nums[q]):
                p = p + 1
                nums[p] = nums[q]
            q = q + 1

        return p + 1