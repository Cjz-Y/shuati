from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        inDegree = [0 for i in range(N + 1)]
        outDegree = [0 for i in range(N + 1)]

        for tru in trust:
            inDegree[tru[1]] += 1
            outDegree[tru[0]] += 1

        ans = -1
        for i in range(1, N + 1):
            if inDegree[i] == N - 1 and outDegree[i] == 0:
                if ans == -1:
                    ans = i
                else:
                    return ans
        return ans



