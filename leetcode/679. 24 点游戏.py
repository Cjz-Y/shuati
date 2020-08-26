from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:

        def merge_two(a, b):
            result = set()
            result.add(a + b)
            result.add(a - b)
            if b != 0:
                result.add(a / b)
            result.add(a * b)
            result.add(b - a)
            if a != 0:
                result.add(b / a)
            return result

        def merge_three(a, list, result):
            for k in list:
                l = merge_two(a, k)
                for ll in l:
                    result.add(ll)

        for i in range(4):
            other_three = nums.copy()
            other_three.remove(nums[i])
            result_three = set()
            for j in range(3):
                other_two = other_three.copy()
                other_two.remove(other_three[j])

                result_two = merge_two(other_two[0], other_two[1])

                merge_three(other_three[j], result_two, result_three)

            result = set()
            merge_three(nums[i], result_three, result)
            for j in result:
                # print(j)
                if abs(j - 24) < 1e-6:
                    return True

        for i in range(4):
            for j in range(i + 1, 4):
                other_two = nums.copy()
                other_two.remove(nums[i])
                other_two.remove(nums[j])

                one = merge_two(nums[i], nums[j])
                two = merge_two(other_two[0], other_two[1])
                for k in one:
                    for l in two:
                        result = merge_two(k, l)
                        for ans in result:
                            # print(ans)
                            if abs(ans - 24) < 1e-6:
                                return True

        return False


if __name__ == '__main__':
    a = [3,3,8,8]

    solution = Solution()

    print(solution.judgePoint24(a))


