from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = []

        def find(left, right, target):
            if left == right:
                return left

            mid = int((left + right) / 2)
            if target > ans[mid]:
                return find(mid + 1, right, target)
            else:
                return find(left, mid, target)

        ans.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                pos = find(0, len(ans) - 1, nums[i])
                ans[pos] = nums[i]
        return len(ans)