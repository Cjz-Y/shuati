from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ans = False

        x_direction = [1, 0, -1, 0]
        y_direction = [0, 1, 0, -1]

        found = set()

        def search(x, y, index):
            if index == len(word):
                return True

            for i in range(4):
                xx = x + x_direction[i]
                yy = y + y_direction[i]
                if 0 <= xx < len(board) and 0 <= yy < len(board[xx]) and (xx, yy) not in found and board[xx][yy] == word[index]:
                    found.add((xx, yy))
                    searched = search(xx, yy, index + 1)
                    if searched:
                        return True
                    found.remove((xx, yy))

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    found.add((i, j))
                    searched = search(i, j, 1)
                    found.remove((i, j))
                    if searched:
                        return True

        return False







