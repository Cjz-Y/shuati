from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:

        def better(a, b):
            # a = str(aa)
            # b = str(bb)

            if len(b) > len(a):
                return not better(b, a)

            for i in range(len(b)):
                if a[i] != b[i]:
                    return a[i] < b[i]

            if len(a) == len(b):
                return True

            return better(a[len(b):], b)


        def quick_sort(left, right):
            if left < right:
                i, j = left, right
                temp = nums[left]
                while i < j:
                    while i < j and better(str(temp), str(nums[j])):
                        j -= 1
                    nums[i] = nums[j]

                    while i < j and better(str(nums[i]), str(temp)):
                        i += 1
                    nums[j] = nums[i]

                nums[i] = temp
                quick_sort(i + 1, right)
                quick_sort(left, i - 1)

        quick_sort(0, len(nums) - 1)

        ans = ''
        for num in nums:
            ans += str(num)

        return ans