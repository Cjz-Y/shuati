from typing import List

# 给定 nums = [3,2,2,3], val = 3,
#
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
#
# 你不需要考虑数组中超出新长度后面的元素
#
# 挂掉的输入为[] 0,

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        end = len(nums) - 1
        while (index <= end):
            if (nums[index] == val):
                nums[index] = nums[end]
                end = end - 1
            else:
                index = index + 1

        return end + 1