from typing import List
import sys
import heapq


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = []
        for i in range(len(nums) - k + 1):
            heapq.heappush(heap, (nums[i], i))

        temp = len(nums) - k + 1
        pre_index = -1
        while temp <= len(nums):
            while heap[0][1] <= pre_index:
                heapq.heappop(heap)
            top = heapq.heappop(heap)
            ans.append(top[0])
            pre_index = top[1]

            if temp == len(nums): break
            heapq.heappush(heap, (nums[temp], temp))
            temp += 1

        return ans
