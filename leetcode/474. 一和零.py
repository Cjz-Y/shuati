from typing import List
from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        f = [[0] * (n + 1) for i in range(m + 1)]

        ans = 0


        cur = [(0, 0)]

        for str in strs:
            counter = Counter(str)

            x = counter.get('0', 0)
            y = counter.get('1', 0)

            next = set()
            for cur_x, cur_y in cur:
                next.add((cur_x, cur_y))
                xx = cur_x + x
                yy = cur_y + y
                if xx <= m and yy <= n:
                    f[xx][yy] = max(f[xx][yy], f[cur_x][cur_y] + 1)
                    ans = max(ans, f[xx][yy])
                    next.add((xx, yy))

            cur = list(next)
            cur.sort(key=lambda item: item[0] + item[1], reverse=True)

        return ans


