import math


class Solution:

    def mySqrt(self, x: int) -> int:
        l, r, anx = 0, x, -1
        while l <= r:
            m = (l + r) // 2
            if m ** 2 <= x:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans





    def mySqrt_math(self, x: int) -> int:
        """
        使用数学的方法来解决这个问题
        :param x:
        :return:
        """
        if x == 0:
            return 0

        index = int(math.exp(0.5 * math.log(x)))
        return index + 1 if (index + 1) ** 2 <= x else index