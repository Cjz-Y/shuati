class Solution:
    def numWays(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        f = [0 for i in range(n + 1)]
        f[0] = 1
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2]) % 1000000007

        return f[n]