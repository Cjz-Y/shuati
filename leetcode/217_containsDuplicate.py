# print(3 ^ 2 ^ 3 ^ 1)
#
# print(1 ^ 2 ^ 3)
#
# print(0 ^ 2)
#
from typing import List

def qsort(head, tail, arr):
    if tail > head :
        i, j = head, tail
        temp = arr[head]
        while i < j:
            while arr[j] >= temp and i < j:
                j -= 1
            arr[i] = arr[j]
            while arr[i] <= temp and i < j:
                i += 1
            arr[j] = arr[i]

        arr[i] = temp
        qsort(head, i - 1, arr)
        qsort(i + 1, tail, arr)

def containsDuplicate(nums: List[int]) -> bool:
    # if len(nums) <= 1:
    #     return False
    #
    # a = nums[0]
    # for i in range(1, len(nums)):
    #     a = a ^ nums[i]
    #     if (a == 0 or a == nums[i]):
    #         return True
    #
    # return False

    # qsort(0, len(nums) - 1, nums)
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i - 1]:
    #         return True
    # return False

    a = set()
    for i in nums:
        if i in a:
            return True
        a.add(i)

    return False




arr = [1,3,2,6,5]
qsort(0, len(arr) - 1, arr)
print(arr)