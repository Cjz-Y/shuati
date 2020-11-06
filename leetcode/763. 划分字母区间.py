from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        pos = {}
        f = [0 for i in range(len(S))]

        for i in range(len(S)):
            temp = pos.get(S[i], -1)
            if temp == -1:
                pos[S[i]] = i
            else:
                f[temp] += 1
                pos[S[i]] = i
                f[i] = -1

        start_index = 0
        ans = []

        lock = 0
        for i in range(len(S)):
            lock += f[i]
            if lock == 0:
                ans.append(i - start_index + 1)
                start_index = i + 1
        return ans
