from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        归并排序的特征：
        1.分为两个部分，后一部分的序号小于前一部分
        2.两个部分都是有序的
        :param nums:
        :return:
        """

        def merge(arr):
            if len(arr) == 1:
                return arr, 0

            mid = len(arr) // 2

            left, left_ans = merge(arr[0:mid])
            right, right_ans = merge(arr[mid:])

            # left中的序号小于right
            left_index = 0
            right_index = 0
            ans = 0
            while left_index < len(left):
                while right_index < len(right) and left[left_index] > 2 * right[right_index]:
                    right_index += 1
                ans += right_index
                left_index += 1

            left_index = 0
            right_index = 0
            sorted_arr = []
            while left_index < len(left) or right_index < len(right):
                if left_index < len(left) and right_index < len(right):
                    if left[left_index] < right[right_index]:
                        sorted_arr.append(left[left_index])
                        left_index += 1
                    else:
                        sorted_arr.append(right[right_index])
                        right_index += 1
                else:
                    if left_index < len(left):
                        sorted_arr.append(left[left_index])
                        left_index += 1
                    else:
                        sorted_arr.append(right[right_index])
                        right_index += 1

            return sorted_arr, ans + left_ans + right_ans

        if len(nums) <= 1:
            return 0
        _, ans = merge(nums)
        return ans
