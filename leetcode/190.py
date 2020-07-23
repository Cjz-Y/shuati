import math

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        n&1 能够获取到二进制最右边的一位
        :param n:
        :return:
        """
        ans, power = 0, 31

        while n != 0:
            ans += (n & 1) << power
            n = n >> 1
            power -= 1
        return ans
