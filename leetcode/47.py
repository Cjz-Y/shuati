from typing import List


class Solution:

    ans = []
    def back(self, nums, result, use: set):
        # print(result)
        if len(result) == len(nums):
            self.ans.append(result.copy())
            return
        for i in range(len(nums)):
            if i not in use and (i == 0 or (i - 1) in use or nums[i] != nums[i - 1]):
                result.append(nums[i])
                use.add(i)
                self.back(nums, result, use)
                result.pop()
                # result.remove(nums[i])
                use.remove(i)


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        self.ans = []
        self.back(nums, [], set())
        return self.ans

if __name__ == '__main__':
    s = Solution()
    a = [2,2,1,1]

    print(s.permuteUnique(a))