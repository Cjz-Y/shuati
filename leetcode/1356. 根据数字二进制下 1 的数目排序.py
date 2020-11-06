from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_one(x):
            # print(x)
            result = 0
            while x != 0:
                x &= (x - 1)
                result += 1
            return result

        def better(a1, b1, a2, b2):
            return a1 > a2 or (a1 == a2 and b1 >= b2)

        def qsort(head, tail, one, two):
            # print(head, tail)
            if head < tail:
                i, j = head, tail
                temp_one = one[head]
                temp_two = two[head]
                while i < j:
                    # print(i, j)
                    while i < j and better(one[j], two[j], temp_one, temp_two): j -= 1
                    one[i] = one[j]
                    two[i] = two[j]

                    while i < j and better(temp_one, temp_two, one[i], two[i]): i += 1
                    one[j] = one[i]
                    two[j] = two[i]
                one[i], two[i] = temp_one, temp_two
                qsort(head, i - 1, one, two)
                qsort(i + 1, tail, one, two)


        count = []

        for num in arr:
            count.append(count_one(num))
        qsort(0, len(count) - 1, count, arr)
        # print(count)
        # print(arr)
        return arr




if __name__ == '__main__':
    a = [0,1,2,3,4,5,6,7,8]
    print(Solution().sortByBits(a))