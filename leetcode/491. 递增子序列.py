from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = []
        result = []

        def find(index):
            if len(result) > 1:
                ans.append(result.copy())
            if index == len(nums):
                return
            use = set()
            for i in range(index, len(nums)):
                if (nums[index] >= result[-1] or len(result) == 0) and nums[index] not in use:
                    use.add(nums[index])
                    result.append(nums[index])
                    find(i + 1)
                    result.pop()


        find(0)
        return ans


