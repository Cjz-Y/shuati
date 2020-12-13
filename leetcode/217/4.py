from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        base = -1
        for num in nums:
            if num % 2 != 0:
                base = max(base, num)
            else:
                if (num // 2) % 2 != 0:
                    base = max(base, num // 2)

        if base == -1:
            return 0
        ans = 0
        min_value = base
        max_value = base
        for num in nums:


            temp = num
            max_diff = abs(temp - base)
            while temp % 2 == 0:
                temp = temp // 2
                diff = abs(temp - base)
                if diff <= max_diff:

                    max_diff = diff
                else:
                    break
            while temp % 2 != 0:
                temp = temp * 2
                diff = abs(temp - base)
                if diff <= max_diff:
                    max_diff = diff
                else:
                    break
            min_value = min(min_value, temp)
            max_value = max(max_value, temp)


        return abs(max_value - min_value)