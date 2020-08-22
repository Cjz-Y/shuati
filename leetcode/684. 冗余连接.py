from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = 0
        for edge in edges:
            size = max(size, max(edge))

        parent = [i for i in range(size + 1)]

        for edge in edges:
            left = edge[0]
            while parent[left] != left:
                parent[left] = parent[parent[left]]
                left = parent[left]

            right = edge[1]
            while parent[right] != right:
                parent[right] = parent[parent[right]]
                right = parent[right]

            if left == right:
                return edge
            else:
                parent[left] = right