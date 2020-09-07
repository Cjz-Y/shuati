from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        find = set()
        current = [0]
        find.add(0)

        while current:
            next = []
            for node in current:
                for point in rooms[node]:
                    if point not in find:
                        find.add(point)
                        next.append(point)
            current = next
        return len(find) == len(rooms)