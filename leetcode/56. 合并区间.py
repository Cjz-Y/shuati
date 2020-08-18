from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        def merge_sort(nums):
            if len(nums) == 1:
                return nums

            mid = int((len(nums) - 1) / 2)
            left_array = merge_sort(nums[0:mid + 1])
            right_array = merge_sort(nums[mid + 1:len(nums)])

            left_index = 0
            right_index = 0
            temp = []
            while left_index < len(left_array) or right_index < len(right_array):
                if left_index < len(left_array) and right_index < len(right_array):
                    left = left_array[left_index]
                    right = right_array[right_index]

                    if left[0] < right[0] or (left[0] == right[0] and left[1] <= right[1]):
                        temp.append(left)
                        left_index += 1
                    else:
                        temp.append(right)
                        right_index += 1
                elif left_index < len(left_array):
                    temp.append(left_array[left_index])
                    left_index += 1
                else:
                    temp.append(right_array[right_index])
                    right_index += 1
            return temp

        sort_arr = merge_sort(intervals)
        print(sort_arr)
        ans = []
        index = 0
        while index < len(sort_arr):
            cur = sort_arr[index]
            while index < len(sort_arr) and cur[1] >= sort_arr[index][0]:
                cur[1] = max(cur[1], sort_arr[index][1])
                index += 1
            ans.append(cur)

        return ans

if __name__ == '__main__':
    a = [[1, 3]]

    b =Solution()
    print(b.merge(a))