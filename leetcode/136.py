from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for x in nums:
            n = n ^ x

        return n