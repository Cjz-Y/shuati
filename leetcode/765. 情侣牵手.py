from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:

        pos = [-1 for i in range(len(row))]

        for i in range(len(row)):
            pos[row[i]] = i

        ans = 0
        for i in range(len(row) // 2):
            print(row)
            one = 2 * i
            two = 2 * i + 1
            # print(one, two)
            if abs(row[one] - row[two]) == 1 and (min(row[one], row[two]) % 2 == 0):
                continue
            else:
                # print(row[one], row[two])
                if row[one] % 2 == 1:
                    find = row[one] - 1
                else:
                    find = row[one] + 1
                find_pos = pos[find]
                row[two], row[find_pos] = row[find_pos], row[two]
                pos[find] = two
                pos[row[find_pos]] = find_pos
                ans += 1
        return ans


if __name__ == '__main__':
    a = [11,5,10,13,4,1,3,7,8,6,12,9,0,2]

    solution = Solution()
    print(solution.minSwapsCouples(a))