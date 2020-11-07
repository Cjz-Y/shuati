from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        def merge(arr):
            # print('arr: ' + str(arr))
            if len(arr) == 1:
                # if lower <= arr[0] <= upper:
                #     return arr, 1
                return arr, 0
            mid = len(arr) // 2

            arr_one, result_one = merge(arr[0: mid])
            arr_two, result_two = merge(arr[mid: len(arr)])
            # print(arr_one, result_one)
            # print(arr_two, result_two)

            l, r = 0, 0
            result = 0
            for i in range(len(arr_one)):
                while l < len(arr_two) and arr_two[l] - arr_one[i] < lower:
                    l += 1
                while r < len(arr_two) and arr_two[r] - arr_one[i] <= upper:
                    r += 1
                if l < len(arr_two):
                    # todo 计算个数
                    if r < len(arr_two):
                        result += (r - l)
                    else:
                        result += (len(arr_two) - l)

            temp = []
            index1, index2 = 0, 0
            while index1 < len(arr_one) or index2 < len(arr_two):
                if index1 < len(arr_one) and index2 < len(arr_two):
                    if arr_one[index1] < arr_two[index2]:
                        temp.append(arr_one[index1])
                        index1 += 1
                    else:
                        temp.append(arr_two[index2])
                        index2 += 1
                elif index1 < len(arr_one):
                    temp.append(arr_one[index1])
                    index1 += 1
                else:
                    temp.append(arr_two[index2])
                    index2 += 1
            return temp, result + result_one + result_two

        f = [0 for i in range(len(nums) + 1)]
        f[0] = 0
        for i in range(1, len(nums) + 1):
            f[i] = f[i - 1] + nums[i - 1]

        # print(f)
        arr, result = merge(f)

        return result




