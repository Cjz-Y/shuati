from typing import List
import collections


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # 就在同一站 不用坐车了
        if S == T:
            return 0
        routes = [set(route) for route in routes]

        edge = collections.defaultdict(set)

        start = set()
        end = set()
        for i in range(len(routes)):
            flag = 0
            sites = routes[i]
            if S in sites:
                start.add(i)
                flag += 1
            if T in sites:
                end.add(i)
                flag += 1

            # 一辆车就坐到了
            if flag == 2:
                return 1

            for j in range(i + 1, len(routes)):
                sites2 = routes[j]
                for _, site in enumerate(sites2):
                    if site in sites:
                        edge[i].add(j)
                        edge[j].add(i)
                        break

        ans = 1
        cur = list(start)
        use = start
        found = False
        while cur:
            next = []
            for cur_bus in cur:

                for index, point in enumerate(edge[cur_bus]):
                    if point not in use:
                        use.add(point)
                        next.append(point)
                        if point in end:
                            found = True
                            break
                if found:
                    break
            cur = next
            ans += 1
            if found:
                break

        if found:
            return ans
        else:
            return -1
