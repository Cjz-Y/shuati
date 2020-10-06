from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:

        # f表示从上一轮比当前小的接着过来的，所以下一轮是要比当前的下的
        f = [0 for i in range(len(A))]
        # g表示从上一轮比当前大的接着过来的，所以下一轮是要比当前大的
        g = [0 for i in range(len(A))]

        f[0] = 1
        g[0] = 1

        ans = 1

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                f[i] = g[i - 1] + 1
                g[i] = 1
            elif A[i] < A[i - 1]:
                g[i] = f[i - 1] + 1
                f[i] = 1
            else:
                f[i] = 1
                g[i] = 1

            ans = max(ans, f[i], g[i])

        return ans