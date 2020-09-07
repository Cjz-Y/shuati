from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        看了题解
        左右遍历获取到当前位置的最大值，
        如果不分块的话，很明显无法完成，因为初始的大值会影响后面的值
        通过分块，使得大值只能在其所能影响的区域里对答案进行影响，而不能超出K的区域

        从左右遍历这个思路出发，很明显碰到的困惑是，如何用一个准确的函数区间来概括当前的滑动窗口
        所以可以认为设置一些中心点，让函数围绕这个中心点来计算
        :param nums:
        :param k:
        :return:
        """
        if not nums:
            return []

        left = [-999999 for i in range(len(nums))]
        for i in range(len(nums)):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

        right = [-999999 for i in range(len(nums))]
        right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            if (i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])

        ans = []
        for i in range(k - 1, len(nums)):
            ans.append(max(left[i], right[i - k + 1]))
        return ans