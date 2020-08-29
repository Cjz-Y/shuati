from typing import List
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:


        edge = {}
        for ticket in tickets:
            point_list = edge.get(ticket[0], [])
            heapq.heappush(point_list, ticket[1])
            edge[ticket[0]] = point_list

        stack = []
        def dfs(node):
            point_list = edge.get(node, [])
            while point_list:
                pop = heapq.heappop(point_list)
                dfs(pop)

            stack.append(node)

        dfs("JFK")
        return stack[::-1]






