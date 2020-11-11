import math
from typing import List

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:

        h, v = destination[1], destination[0]
        ans = ""
        for i in range(h + v):
            if h > 0:

                time = math.comb(h + v - 1, h - 1)
                if k > time:
                    ans = ans + "V"
                    k -= time
                    v -= 1
                else:
                    ans = ans + "H"
                    h -= 1
            else:
                ans = ans + "V"
                v -= 1

        return ans



