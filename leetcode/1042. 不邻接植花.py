from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flower = [-1 for i in range(N + 1)]

        nei = [set() for i in range(N + 1)]

        point_list = [[] for i in range(N + 1)]

        for path in paths:
            point_list[path[0]].append(path[1])
            point_list[path[1]].append(path[0])

        for i in range(1, N + 1):
            fl = -1
            for fl in range(1,5):
                if fl not in nei[i]:
                    break
            flower[i] = fl
            for point in point_list[i]:
                nei[point].add(fl)


        return flower[1:]
