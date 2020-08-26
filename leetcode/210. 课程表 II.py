from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depen = [set() for i in range(numCourses)]
        f = [0 for i in range(numCourses)]

        for i in range(len(prerequisites)):
            depen[prerequisites[i][1]].add(prerequisites[i][0])
            f[prerequisites[i][0]] += 1

        learned = []
        for i in range(numCourses):
            if f[i] == 0:
                learned.append(i)

        index = 0
        while index < len(learned):
            for i in depen[learned[index]]:
                f[i] -= 1
                if f[i] == 0:
                    learned.append(i)
            index += 1

        if len(learned) == numCourses:
            return learned
        else:
            return []

if __name__ == '__main__':
    a = 4
    b = [[1, 0], [2, 0], [3, 1], [3, 2]]

    solution = Solution()
    print(solution.findOrder(a, b))