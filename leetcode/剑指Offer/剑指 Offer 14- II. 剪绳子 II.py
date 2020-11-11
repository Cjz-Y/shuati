class Solution:
    def cuttingRope(self, n: int) -> int:
        mod_value = 1000000007

        f = [0 for i in range(n + 1)]

        if n == 2:
            return 1
        elif n == 3:
            return 2


        for i in range(1, n + 1):
            f[i] = i
            for k in range(1, (i // 2) + 1):
                f[i] = max(f[i], f[k] * f[i - k])

        return f[n] % mod_value
