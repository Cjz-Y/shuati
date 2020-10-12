import math
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        f = []
        for i in range(1, int(math.pow(10, n))):
            f.append(i)
        return f