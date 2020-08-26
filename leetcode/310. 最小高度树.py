from typing import List


class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        从树的叶子节点bfs遍历整棵树
        1.枚举所有的边
        2.找到入度为0的边
        3.以这些点为基础枚举他们的出度，然后减去相对应入度
        4.找到当前入度为1的点，进入队列（入度为1相当于当前的最外层），找到最后入度为1的点
        :param n:
        :param edges:
        :return:
        """
        if n == 1:
            return [0]
        out = [[] for i in range(n)]
        for edge in edges:
            out[edge[0]].append(edge[1])
            out[edge[1]].append(edge[0])

        current = []
        for i in range(n):
            if len(out[i]) == 1:
                current.append(i)

        while current:
            next = []
            for node in current:
                for i in range(len(out[node])):
                    child = out[node][i]
                    out[child].remove(node)
                    if len(out[child]) == 1:
                        next.append(child)
            if not next:
                break
            current = next
        return current






    def _findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        超时解，floyd计算每个节点之间的距离
        :param n:
        :param edges:
        :return:
        """
        null = 9999999
        dist = [[null] * n for i in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for edge in edges:
            dist[edge[0]][edge[1]] = 1
            dist[edge[1]][edge[0]] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                    if dist[j][k] + dist[k][i] < dist[j][i]:
                        dist[j][i] = dist[j][k] + dist[k][i]

        ans = []
        ans_value = null
        for i in range(n):
            max_value = max(dist[i])
            if ans_value == null or max_value == ans_value:
                ans.append(i)
            elif max_value < ans_value:
                ans_value = max_value
                ans.clear()
                ans.append(i)
        return ans


