from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        def back(index, result, sum_value):
            if len(result) == 4:
                if sum_value == target:
                    ans.append(result.copy())

                return

            if sum_value + sum(nums[len(nums) - (4 - len(result)):]) < target:
                return
            if sum_value + sum(nums[index:index + (4 - len(result))]) > target:
                return

            if index >= len(nums):
                return
            use = set()
            for i in range(index, len(nums)):
                if nums[i] not in use:
                    use.add(nums[i])
                    result.append(nums[i])
                    back(i + 1, result, sum_value + nums[i])
                    result.pop()


        nums.sort()

        back(0, [], 0)

        return ans