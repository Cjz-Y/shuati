from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def search(index, num, result):
            if num == k:
                ans.append(result.copy())
                return
            else:
                for i in range(index, n + 1):
                    result.append(i)
                    search(i + 1, num + 1, result)
                    result.pop()


        search(1, 0, [])
        return ans