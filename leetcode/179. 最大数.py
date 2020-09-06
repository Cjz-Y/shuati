from typing import List


class Solution:


    def largestNumber(self, nums: List[int]) -> str:

        def better(a, b):
            if a == b:
                return True
            c, d = str(a), str(b)
            swap = False
            if len(c) < len(d):
                c, d = d, c
                swap = True

            temp_c = c[:len(d)]
            if temp_c != d:
                if swap:
                    return not temp_c > d
                else:
                    return temp_c > d
            else:
                flag = better(c[len(d):], d)
                if swap:
                    return not flag
                else:
                    return flag


        def quick_sort(left, right):
            if right > left:
                i, j = left, right
                temp = nums[left]
                while i < j:
                    while i < j and better(temp, nums[j]):
                        j -= 1
                    nums[i] = nums[j]
                    while i < j and better(nums[i], temp):
                        i += 1
                    nums[j] = nums[i]
                nums[i] = temp
                quick_sort(i + 1, right)
                quick_sort(left, i - 1)


        quick_sort(0, len(nums) - 1)
        # print(nums)
        temp = ''
        for i in nums:
            temp += str(i)
        return temp




if __name__ == '__main__':
    a = 9223
    b = 9223

    c = [3,30,34,5,9]

    # print(Solution().better(a, b))
    print(Solution().largestNumber(c))
