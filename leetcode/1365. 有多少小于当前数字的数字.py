from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        def better(ai, bi, aj, bj):
            # return ai > aj or (ai == aj and (bi >= bj))
            return ai >= aj

        def qsort(head, tail, a, b):
            if head < tail:
                i, j = head, tail
                tempa = a[head]
                tempb = b[head]
                while i < j:
                    while i < j and better(a[j], b[j], tempa, tempb): j -= 1
                    a[i] = a[j]
                    b[i] = b[j]

                    while i < j and better(tempa, tempb, a[i], b[i]): i += 1
                    a[j] = a[i]
                    b[j] = b[i]
                a[i] = tempa
                b[i] = tempb

                qsort(head, i - 1, a, b)
                qsort(i + 1, tail, a, b)


        pos = [i for i in range(len(nums))]
        qsort(0, len(nums) - 1, nums, pos)

        # print(nums)
        # print(pos)

        f = [0] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                f[i] = i
            else:
                f[i] = f[i - 1]

        qsort(0, len(nums) - 1, pos, f)

        return f


if __name__ == '__main__':
    a = [8,1,2,2,3]

    print(Solution().smallerNumbersThanCurrent(a))