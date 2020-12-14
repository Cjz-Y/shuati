class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 2:
            return 0

        f = [0 for i in range(len(nums))]


        for i in range(len(nums)):
            if i % 2 == 0:
                if i == 0:
                    f[i] = nums[i]
                else:
                    f[i] = f[i - 2] + nums[i]
            else:
                if i == 1:
                    f[i] = nums[i]
                else:
                    f[i] = f[i - 2] + nums[i]

        last_ou_index = len(nums) - 1 if (len(nums) - 1) % 2 == 0 else len(nums) - 2
        last_ji_index = len(nums) - 2 if (len(nums) - 1) % 2 == 0 else len(nums) - 1
        ans = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                pre_ou = 0 if i == 0 else f[i - 2]
                after_ou = f[last_ou_index] - f[i]
                pre_ji = 0 if i == 0 else f[i - 1]
                after_ji = f[last_ji_index] if i == 0 else f[last_ji_index] - f[i - 1]

                if pre_ou + after_ji == pre_ji + after_ou:
                    ans += 1
            else:
                pre_ou = f[i - 1]
                after_ou = f[last_ou_index] - f[i - 1]
                pre_ji = 0 if i == 1 else f[i - 2]
                after_ji = f[last_ji_index] - f[i]
                if pre_ou + after_ji == pre_ji + after_ou:
                    ans += 1
        return ans
