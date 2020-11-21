from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        def qsort(head, tail, one, two):
            if tail > head:
                i, j = head, tail
                temp_one, temp_two = one[head], two[head]
                while i < j:
                    while (one[j] > temp_one or (one[j] == temp_one and two[j] >= temp_two)) and i < j:
                        j -= 1
                    one[i] = one[j]
                    two[i] = two[j]
                    while (one[i] < temp_one or (one[i] == temp_one and two[i] <= temp_two)) and i < j:
                        i += 1
                    one[j] = one[i]
                    two[j] = two[i]

                one[i] = temp_one
                two[i] = temp_two
                qsort(head, i - 1, one, two)
                qsort(i + 1, tail, one, two)

        qsort(0, len(scores) - 1, ages, scores)
        # print(ages)
        # print(scores)

        f = [scores[i] for i in range(len(scores))]
        # g = [-1 for i in range(len(scores))]
        # ans_index = -1
        ans = 0
        for i in range(len(scores)):
            for j in range(i):
                # print(ages[i], ages[j], scores[i], scores[j])
                # print('年龄：' + str(ages[i]) + " " + str(ages[j]))
                # print('分数：' + str(scores[i]) + " " + str(scores[j]))
                if not (ages[j] < ages[i] and scores[j] > scores[i]):
                    # print('enter')
                    # f[i] = max(f[i], f[j] + scores[i])
                    if f[j] + scores[i] > f[i]:
                        f[i] = f[j] + scores[i]
                        # g[i] = j

            # ans = max(ans, f[i])
            if f[i] > ans:
                # ans_index = i
                ans = f[i]
        # print(ans_index)

        while ans_index != -1:
            print(ages[ans_index], scores[ans_index])
            ans_index = g[ans_index]

        return ans



if __name__ == '__main__':
    # scores = [41, 33, 53, 102, 15]
    # ages = [11, 42, 32, 4, 55]
    # scores = [2,1,2,4,5]
    # ages = [1,2,2,3,4]

    scores = [722, 235, 424, 711, 508, 881, 21, 126, 828, 679, 826, 264, 318, 284, 778, 409, 658, 10, 502, 609, 452, 552, 45, 926, 376, 229, 463]
    ages = [10, 95, 26, 25, 16, 58, 90, 84, 47, 17, 31, 54, 7, 10, 63, 25, 65, 16, 31, 57, 24, 13, 81, 36, 1, 25, 6]

    Solution().bestTeamScore(scores, ages)

