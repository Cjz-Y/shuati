class Solution:
    def minCut(self, s: str) -> int:
        f = [[99999] * len(s) for i in range(len(s))]
        # 1/3
        for i in range(len(s)):
            f[i][i] = 0
            if i < len(s) - 1 and i > 0 and s[i - 1] == s[i + 1]:
                f[i - 1][i + 1] = 0
        # 2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                f[i][i + 1] = 0

        # 多len
        for length in range(0, len(s) - 1):
            for start in range(0, len(s) - length):
                end = start + length
                if f[start][end] == 0 and end < len(s) - 1 and start > 0 and s[start - 1] == s[end + 1]:
                    f[start - 1][end + 1] = 0
                # if start > 0 and end < len(s) - 1:
                #     print("start = %d, end = %d, f = %d, s[start - 1] = %s, s[end + 1] = %s" % (start, end, f[start][end], s[start - 1], s[end + 1]))

        if f[0][len(s) - 1] == 0:
            return 0

        # for l in f:
        #     print(l)

        ans = [99999 for i in range(len(s))]
        # 以j结尾的最长的
        for i in range(len(s)):
            if f[0][i] == 0:
                ans[i] = 0
                continue
            for j in range(i):
                if f[j + 1][i] == 0:
                    ans[i] = min(ans[i], ans[j] + 1)
                else:
                    ans[i] = min(ans[i], ans[j] + i - j)



        # for i in range(2, len(s) + 1):
        #     for start in range(len(s) - i + 1):
        #         end = start + i - 1
        #
        #         for mid in range(start, end):
        #             f[start][end] = min(f[start][end], f[start][mid] + f[mid + 1][end] + 1)

        return ans[len(s) - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCut('ab'))

