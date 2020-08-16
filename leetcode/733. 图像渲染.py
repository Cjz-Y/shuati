from typing import List


class Solution:

    def dfs(self, x, y):
        for i in range(4):
            xx = x + self.process_x[i]
            yy = y + self.process_y[i]
            if 0 <= xx < len(self.image) and 0 <= yy < len(self.image[xx]) and self.image[xx][yy] == self.target:
                self.image[xx][yy] = self.newColor
                self.dfs(xx, yy)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        self.process_x = [1, 0, -1, 0]
        self.process_y = [0, 1, 0, -1]
        self.newColor = newColor
        self.image = image
        self.target = image[sr][sc]

        image[sr][sc] = newColor
        self.dfs(sr, sc)

        return self.image

