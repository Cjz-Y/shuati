from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        null = 99999
        dist = [[null] * (K + 2) for i in range(n)]

        dist[src][0] = 0

        edge = [[] for i in range(n)]

        for item in flights:
            edge[item[0]].append((item[1], item[2]))

        cur = [(src, 0)]
        while cur:
            next = []
            use = set()
            for (cur_node, cur_time) in cur:

                for point, value in edge[cur_node]:
                    if cur_time + 1 < K + 2 and dist[cur_node][cur_time] + value < dist[point][cur_time + 1]:
                        dist[point][cur_time + 1] = dist[cur_node][cur_time] + value

                        if (point, cur_time + 1) not in use:
                            use.add((point, cur_time + 1))
                            next.append((point, cur_time + 1))

            cur = next

        ans = min(dist[dst])

        return ans if ans != null else -1

