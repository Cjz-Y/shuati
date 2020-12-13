from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:


        def back(pre_mask, pre):
            for i in range(pre + 1, len(nums)):
                if pre_mask & 1 << i == 1:
                    if pre != 0 and

        null = 9999999
        init_mask = 2 ** (len(nums)) - 1
        f = [[null for j in range(len(nums))] for i in range(init_mask + 2)]

        f[init_mask][0] = 0
        nums.sort()

        for i in range(init_mask + 1)
