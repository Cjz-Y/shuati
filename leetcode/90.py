from typing import List


class Solution:
    ans = []
    def back(self, cur, nums, result):
        # print('cur = %d' % cur)
        if cur == len(nums):
            return
        for i in range(cur, len(nums)):
            # print('i = %d' % i)
            if i == cur or nums[i] != nums[i - 1]:

                result.append(nums[i])
                self.back(i + 1, nums, result)
                self.ans.append(result.copy())
                # print(result)
                result.remove(nums[i])


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = [[],]
        self.back(0, nums, [])
        return self.ans


if __name__ == '__main__':
    a = [1,2,2]

    s = Solution()

    print(s.subsetsWithDup(a))