from typing import List

def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    sum = int((1 + n) * n / 2)
    for i in nums:
        sum -= i
    return sum