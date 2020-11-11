from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def search(index, result, sum_value):
            if sum_value == target:
                ans.append(result.copy())
                return

            use = set()
            for i in range(index, len(candidates)):
                if sum_value + candidates[i] > target:
                    break
                if candidates[i] not in use:
                    use.add(candidates[i])
                    result.append(candidates[i])
                    search(i + 1, result, sum_value + candidates[i])
                    result.pop()



        candidates.sort()
        ans = []

        search(0, [], 0)

        return ans