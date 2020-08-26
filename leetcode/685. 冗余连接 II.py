from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        two_in_degree = False
        two = -1
        in_degree = {}
        size = 0
        for edge in edges:
            size = max(size, max(edge))
            if edge[1] in in_degree.keys():
                two_in_degree = True
                in_degree[edge[1]].append(edge[0])
                two = edge[1]
            else:
                in_degree[edge[1]] = [edge[0]]

        # 如果图中有个点有两个入度，那么先将这两个入度排除构建树，最后再将其中一条边加入其中，如果成环就返回这条边，如果不成环就返回另一条边
        if two_in_degree:
            parent = [i for i in range(size + 1)]

            for edge in edges:
                if edge[1] != two:
                    parent[edge[1]] = edge[0]

            father = in_degree[two][0]
            temp = father
            while parent[temp] != temp:
                temp = parent[temp]
            if temp == two:
                return [in_degree[two][0], two]
            else:
                return [in_degree[two][1], two]
        # 如果图中节点都只有一个入度，那么将成环的最后一条边返回
        else:
            parent = [i for i in range(size + 1)]

            for edge in edges:
                father = edge[0]
                while parent[father] != father:
                    father = parent[father]
                if father != edge[1]:
                    parent[edge[1]] = edge[0]
                else:
                    return edge



