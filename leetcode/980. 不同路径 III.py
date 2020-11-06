from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def search(x, y):
            print(x, y)
            if x == end_x and y == end_y:
                if len(use) == total + 1:
                    nonlocal ans
                    ans += 1
                return
            for i in range(4):
                new_x = x + temp_x[i]
                new_y = y + temp_y[i]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[new_x]) and grid[new_x][new_y] != -1 and (new_x, new_y) not in use:
                    use.add((new_x, new_y))
                    search(new_x, new_y)
                    use.remove((new_x, new_y))

        start_x, start_y = -1, -1
        end_x, end_y = -1, -1
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                if grid[i][j] == 2:
                    end_x, end_y = i, j
                if grid[i][j] == 0:
                    total += 1

        ans = 0
        temp_x = [1, 0, -1, 0]
        temp_y = [0, 1, 0, -1]
        use = set()
        use.add((start_x, start_y))

        search(start_x, start_y)

        return ans

