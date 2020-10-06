from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:

        mi = 20
        ma = -5
        use = set()
        for num in nums:
            if num == 0:
                continue
            else:
                if num in use:
                    return False
                else:
                    use.add(num)
                    mi = min(mi, num)
                    ma = max(ma, num)

        return ma - mi < 5