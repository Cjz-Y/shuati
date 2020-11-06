from typing import List
import collections


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)

        counter = list(counter.items())

        counter.sort(key=lambda x: (x[1], -x[0]))

        ans = []
        for key, time in counter:
            for j in range(time):
                ans.append(key)
        return ans