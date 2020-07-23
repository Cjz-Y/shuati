class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            # n & (n - 1)可以用来移除最后二进制中最后一个1
            n = n & (n - 1)
            ans += 1

        return ans
