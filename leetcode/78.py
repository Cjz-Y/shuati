from typing import List


class Solution:

    def back_process(self, current, current_index, nums, result):
        if current_index == len(nums) - 1:
            return

        for i in range((current_index + 1), len(nums)):
            temp = current.copy()
            temp.append(nums[i])
            result.append(temp)
            self.back_process(temp, i, nums, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        self.back_process([], -1, nums, result)
        return result

s = Solution()
print(s.subsets([1,2,3]))