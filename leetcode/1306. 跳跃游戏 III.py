from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        find = set()
        find.add(start)

        current = [start]
        while current:
            next = []
            for node in current:
                if node + arr[node] < len(arr) and (node + arr[node]) not in find:
                    next.append(node + arr[node])
                    find.add(node + arr[node])
                    if arr[node + arr[node]] == 0:
                        return True
                if node - arr[node] >= 0 and (node - arr[node]) not in find:
                    next.append(node - arr[node])
                    find.add(node - arr[node])
                    if arr[node - arr[node]] == 0:
                        return True

            current = next

        return False