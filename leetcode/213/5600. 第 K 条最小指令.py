from typing import List


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        time = 0
        target_x, target_y = destination[0], destination[1]
        ans = ""

        def search(x, y, path):
            nonlocal ans, time

            if x == target_x and y == target_y:

                time += 1
                if time == k:
                    ans = path
                    return
                return

            if y + 1 <= target_y:
                search(x, y + 1, path + "H")
            if ans != "":
                return
            if x + 1 <= target_x:
                search(x + 1, y, path + "V")
            if ans != "":
                return

        search(0, 0, "")

        return ans
