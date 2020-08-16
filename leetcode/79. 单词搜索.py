from typing import List


class Solution:

    def back(self, use, x, y, index, word, board):
        # print(x, y, word[:index])
        if index == len(word):
            self.ans = True
            return

        for i in range(4):
            xx = x + self.process_x[i]
            yy = y + self.process_y[i]
            if 0 <= xx < len(board) and 0 <= yy < len(board[xx]) and (xx, yy) not in use and board[xx][yy] == word[index]:
                use.add((xx, yy))
                self.back(use, xx, yy, index + 1, word, board)
                if self.ans:
                    return
                use.remove((xx,yy))



    def exist(self, board: List[List[str]], word: str) -> bool:
        self.process_x = [1, 0, -1, 0]
        self.process_y = [0, 1, 0, -1]
        self.ans = False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    use = set()
                    use.add((i, j))
                    self.back(use, i, j, 1, word, board)
                    if self.ans:
                        return self.ans

        return self.ans


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "E", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"

    solution = Solution()
    print(solution.exist(board, word))