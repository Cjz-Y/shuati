from typing import List
import collections


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:

        def make(used):
            temp = list(used)
            temp.sort()
            result = [str(x) for x in temp]
            return ''.join(result)

        ans = -1

        used = [set() for i in range(k)]
        pattern_used = [set() for i in range(k)]
        m = len(nums) // k

        def back(index):
            if index >= len(nums):
                nonlocal ans
                temp = 0
                print('start')
                for i in range(k):
                    print(used[i])
                    temp += (max(used[i]) - min(used[i]))
                print(temp)
                if ans == -1 or temp < ans:
                    ans = temp
                return

            for i in range(k):
                if nums[index] not in used[i] and len(used[i]) < m:
                    used[i].add(nums[index])
                    if len(used[i]) == m:
                        mark = make(used[i])
                        print(mark, mark not in pattern_used[i])
                        if mark not in pattern_used[i]:
                            pattern_used[i].add(mark)
                            back(index + 1)
                    else:
                        back(index + 1)

                    used[i].remove(nums[index])

        back(0)

        return ans
