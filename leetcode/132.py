class Solution:
    def minCut(self, s: str) -> int:
        f = [[99999] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            f[i][i] = 0

        for i in range(2, len(s) + 1):
            for start in range(len(s) - i + 1):
                end = start + i - 1
                huiwen = True
                for mid in range(int(i / 2)):
                    if s[start + mid] != s[end - mid]:
                        huiwen = False
                        break

                if huiwen:
                    f[start][end] = 0
                    continue

                for mid in range(start, end):
                    f[start][end] = min(f[start][end], f[start][mid] + f[mid + 1][end] + 1)

                # print('start  = %d, end = %d, f = %d' % (start, end, f[start][end]))

        return f[0][len(s) - 1]
