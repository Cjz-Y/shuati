from typing import List
import heapq


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        learned = []

        in_degree = [0 for i in range(numCourses)]
        edges = [[] for i in range(numCourses)]
        for edge in prerequisites:
            in_degree[edge[1]] += 1
            edges[edge[0]].append(edge[1])

        for i in range(numCourses):
            if in_degree[i] == 0:
                learned.append(i)

        index = 0
        while index < len(learned):
            node = learned[index]
            for i in range(len(edges[node])):
                point = edges[node][i]
                in_degree[point] -= 1
                if in_degree[point] == 0:
                    learned.append(point)

            index += 1

        return True if len(learned) == numCourses else False
