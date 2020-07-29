from typing import List


class Solution:
    ans = []

    def back(self, cur, nums, result, sum, target):
        # print(result)
        if sum == target:
            self.ans.append(result.copy())
            return
        if cur == len(nums):
            return
        for i in range(cur, len(nums)):
            if sum + nums[i] > target:
                return
            result.append(nums[i])
            sum += nums[i]
            self.back(i, nums, result, sum, target)
            result.pop()
            sum -= nums[i]



    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.back(0, candidates, [], 0, target)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    a = [2,3,6,7]

    print(s.combinationSum(a, 7))