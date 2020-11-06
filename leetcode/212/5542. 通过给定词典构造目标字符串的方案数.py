from typing import List
import math

class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        mod = math.pow(10, 9) + 7

        time = []
        for i in range(len(words[0])):
            counter = {}
            for j in range(len(words)):
                counter[words[j][i]] = counter.get(words[j][i], 0) + 1
            time.append(counter)

        f = [[0] * len(words[0]) for j in range(len(target))]
        # print(f)
        for i in range(len(target)):
            for j in range(i, len(words[0])):
                # print(i, j)
                if i == 0:
                    f[i][j] = (time[j].get(target[i], 0)) % mod
                    if j != 0:
                        f[i][j] = (f[i][j] + f[i][j - 1])  % mod
                else:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j - 1] * time[j].get(target[i], 0)) % mod
        return f[len(target) - 1][len(words[0]) - 1]