from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        graph_reversed = [[] for i in range(len(graph))]

        indegree = [0 for i in range(len(graph))]

        ans = []

        for i in range(len(graph)):
            point_list = graph[i]
            indegree[i] = len(graph[i])
            if indegree[i] == 0:
                ans.append(i)
            for point in point_list:
                graph_reversed[point].append(i)

        # print(ans)

        index = 0
        while index < len(ans):
            node = ans[index]
            point_list = graph_reversed[node]
            for point in point_list:
                indegree[point] -= 1
                if indegree[point] == 0:
                    ans.append(point)
            index += 1

        ans.sort()
        return ans



    def _eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Kosaraju 求强连通分量，然后找连通分量为1的，但是如果数据中有自环，也就是自己连接自己，那么判断不出来，因为他是连通分量却不是安全节点
        :param graph:
        :return:
        """
        def dfs(node, edge, f=False):
            for point in edge[node]:
                if point not in find:
                    find.add(point)
                    dfs(point, edge, f)
            if f:
                stack.append(node)

        graph_reversed = [[] for i in range(len(graph))]

        for i in range(len(graph)):
            point_list = graph[i]
            for point in point_list:
                graph_reversed[point].append(i)

        print(graph_reversed)

        find = set()
        stack = []

        for i in range(len(graph)):
            if i not in find:
                find.add(i)
                dfs(i, graph_reversed, True)

        print(stack)

        ans = []
        find = set()
        while stack:
            cur = stack.pop()
            while stack and cur in find:
                cur = stack.pop()
            pre = len(find)
            find.add(cur)
            dfs(cur, graph)

            if len(find) - pre == 1:
                ans.append(cur)

        ans.sort()
        return ans

if __name__ == '__main__':
    a = [[1,2],[2,3],[5],[0],[5],[],[]]

    solution = Solution()
    print(solution.eventualSafeNodes(a))