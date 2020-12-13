
class Solution:
    def concatenatedBinary(self, n: int) -> int:

        # def bitCount(m):
        #     ans = 0
        #     temp = m
        #     while m != 0:
        #         m = m >> 1
        #         ans += 1
        #     return ans

        mod = 10 ** 9 + 7


        bitNumber = 1
        threshold = 2 ** (bitNumber - 1)
        timeCount = 0

        temp = 0
        for i in range(1, n + 1):
            temp = ((temp << bitNumber) + i) % mod

            timeCount += 1
            if timeCount >= threshold:
                bitNumber += 1
                threshold = 2 ** (bitNumber - 1)
                timeCount = 0

        return temp

