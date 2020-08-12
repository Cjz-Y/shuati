from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dic = {}
        for i in nums1:
            dic[i] = dic.get(i, 0) + 1

        ans = []

        for i in nums2:
            num = dic.get(i, 0)
            if num != 0:
                ans.append(i)
                dic[i] = dic.get(i, 0) - 1
        return ans