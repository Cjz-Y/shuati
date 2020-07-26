class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        f = [[0] * len(text2) for i in range(len(text1))]


        for i in range(len(text1)):
            for j in range(len(text2)):
                if i > 0:
                    f[i][j] = max(f[i][j], f[i - 1][j])
                if j > 0:
                    f[i][j] = max(f[i][j], f[i][j - 1])
                if i == 0 or j == 0:
                    last = 0
                else:
                    last = f[i - 1][j - 1]
                if text1[i] == text2[j]:
                    f[i][j] = max(f[i][j], last + 1)

        return f[len(text1) - 1][len(text2) - 1]

if __name__ == '__main__':
    a = 'intention'
    b = 'execution'

    s = Solution()
    print(s.longestCommonSubsequence(a,b))