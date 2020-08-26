from typing import List
import heapq


class Solution:

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        null = 999999

        edges = [[] for i in range(N + 1)]
        for time in times:
            edges[time[0]].append(time)

        g = [(0, K)]

        def push(value):
            g.append(value)

            index = len(g) - 1
            father = ((index + 1) // 2) - 1
            while father >= 0 and g[father][0] > g[index][0]:
                g[father], g[index] = g[index], g[father]
                index = father
                father = ((index + 1) // 2) - 1

        def pop():
            g[0], g[len(g) - 1] = g[len(g) - 1], g[0]
            return_item = g.pop()

            index = 0
            child = index * 2 + 1
            while child < len(g):
                right = child + 1
                if right < len(g) and g[child][0] > g[right][0]:
                    child = right
                if g[index][0] > g[child][0]:
                    g[child], g[index] = g[index], g[child]
                    index = child
                    child = index * 2 + 1
                else:
                    break

            return return_item




        dist = {}
        while g:
            dis, node = pop()
            if node in dist:
                continue
            dist[node] = dis
            for edge in edges[node]:
                if edge[1] not in dist:
                    push((dis + edge[2], edge[1]))

        return max(dist.values()) if len(dist) == N else -1



    def networkDelayTime_ff(self, times: List[List[int]], N: int, K: int) -> int:
        null = 999999
        f = [null] * (N + 1)

        edges = [[] for i in range(N + 1)]
        for time in times:
            edges[time[0]].append(time)

        f[K] = 0
        update = [K]
        while not update:
            next = []
            for update_node in update:
                for edge in edges[update_node]:
                    if f[update_node] + edge[2] < f[edge[1]]:
                        next.append(edge[1])
                        f[edge[1]] = f[update_node] + edge[2]
            update = next

        del f[0]
        ans = max(f)
        return ans if ans != null else -1