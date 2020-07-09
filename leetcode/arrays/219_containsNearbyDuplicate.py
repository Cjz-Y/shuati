from typing import List

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # map = {}
    # for i in range(len(nums)):
    #     if nums[i] in map:
    #         if abs(i - map.get(nums[i])) <= k:
    #             return True
    #     map[nums[i]] = i
    # return False


    a = set()
    for i in range(len(nums)):
        if nums[i] in a:
            return True
        a.add(nums[i])
        if len(a) > k:
            a.remove(nums[i - k])

    return False