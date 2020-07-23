from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = []
        for i in range(num + 1):
            ans_item = 0
            n = i
            while n != 0:
                n = n & (n - 1)
                ans_item += 1
            ans.append(ans_item)

        return ans