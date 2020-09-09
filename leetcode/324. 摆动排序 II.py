from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quick_select(begin, end):
            temp = nums[begin]
            i, j = begin, end
            while i < j:
                while i < j and nums[j] >= temp:
                    j -= 1
                nums[i] = nums[j]

                while i < j and nums[i] <= temp:
                    i += 1
                nums[j] = nums[i]
            nums[i] = temp
            if i == len(nums) // 2:
                return i
            elif i > len(nums) // 2:
                return quick_select(begin, i - 1)
            else:
                return quick_select(i + 1, end)

        mid = quick_select(0, len(nums) - 1)
        middle = nums[mid]
        # print(nums)

        if len(nums) % 2 == 0:
            a = nums[:(len(nums) // 2)]
            b = nums[(len(nums) // 2):]

        else:
            a = nums[:(len(nums) // 2) + 1]
            b = nums[(len(nums)// 2) + 1:]


        # 将=mid的数放中间
        index_end = len(a) - 1
        index = 0
        while index < index_end:
            if a[index] == middle:
                a[index], a[index_end] = a[index_end], a[index]
                index_end -= 1
            else:
                index += 1

        index_begin = 0
        index = len(b) - 1
        while index > index_begin:
            if b[index] == middle:
                b[index], b[index_begin] = b[index_begin], b[index]
                index_begin += 1
            else:
                index -= 1

        index = 0
        while index < len(nums):
            if index % 2 == 0:
                nums[index] = a.pop()
            else:
                nums[index] = b.pop()
            index += 1



if __name__ == '__main__':
    a = [3,2,1,1,3,2]
    print(Solution().wiggleSort(a))



