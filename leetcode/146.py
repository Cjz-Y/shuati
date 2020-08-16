from typing import List


class Solution:
    ans = []
    def back(self, nums, result, use: set):
        # print(result)
        if len(result) == len(nums):
            self.ans.append(result.copy())
            return
        for item in nums:
            if item not in use:
                result.append(item)
                use.add(item)
                self.back(nums, result, use)
                result.remove(item)
                use.remove(item)


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.back(nums, [], set())
        return self.ans


if __name__ == '__main__':
    s = Solution()

    a = [1,2,3]
    print(s.permute(a))