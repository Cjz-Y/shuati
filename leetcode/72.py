class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "":
            return len(word2)
        if word2 == '':
            return len(word1)

        f = [[99999] * len(word2) for i in range(len(word1))]

        for i in range(len(word1)):
            for j in range(len(word2)):
                if i > 0:
                    f[i][j] = min(f[i][j], f[i - 1][j] + 1)
                if j > 0:
                    f[i][j] = min(f[i][j], f[i][j - 1] + 1)
                if word1[i] == word2[j]:
                    if i == 0 and j == 0:
                        f[i][j] = 0
                    elif j == 0:
                        f[i][j] = min(f[i][j], i)
                    elif i == 0:
                        f[i][j] = min(f[i][j], j)
                    elif i > 0 and j > 0:
                        f[i][j] = min(f[i][j], f[i - 1][j - 1])
                else:
                    if i == 0 and j == 0:
                        f[i][j] = 1
                    elif i == 0:
                        f[i][j] = min(f[i][j], j + 2)
                    elif j == 0:
                        f[i][j] = min(f[i][j], i + 2)
                    elif i > 0 and j > 0:
                        f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)

        return f[len(word1) - 1][len(word2) - 1]


