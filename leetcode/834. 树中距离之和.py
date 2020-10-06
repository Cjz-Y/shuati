from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:


        def dfs(x, father):
            for son in edge[x]:
                if son == father:
                    continue
                dfs(son, x)
                nodeNumber[x] += nodeNumber[son]
                dist[x] += (dist[son] + nodeNumber[son])

            nodeNumber[x] += 1


        def dfs2(x, father):
            ans[x] = dist[x]
            for son in edge[x]:
                if son == father:
                    continue

                pdx = dist[x]
                pnx = nodeNumber[x]
                pds = dist[son]
                pns = nodeNumber[son]

                dist[x] -= (dist[son] + nodeNumber[son])
                nodeNumber[x] -= nodeNumber[son]
                dist[son] += (dist[x] + nodeNumber[x])
                nodeNumber[son] += nodeNumber[x]
                dfs2(son, x)

                dist[x] = pdx
                nodeNumber[x] = pnx
                dist[son] = pds
                nodeNumber[son] = pns





        edge = [[] for i in range(N)]

        for item in edges:
            edge[item[0]].append(item[1])
            edge[item[1]].append(item[0])

        nodeNumber = [0 for i in range(N)]
        dist = [0 for i in range(N)]

        dfs(0, 0)

        ans = [0 for i in range(N)]

        dfs2(0, 0)

        return ans



