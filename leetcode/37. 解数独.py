from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        vertical = [set() for i in range(len(board))]
        horizontal = [set() for i in range(len(board))]
        little = [set() for i in range(9)]

        def get_little_index(x, y):
            if x < 3:
                little_index = y // 3
            elif x < 6:
                little_index = 3 + y // 3
            else:
                little_index = 6 + y // 3
            return little_index

        def add(x, y, i):
            board[x][y] = i

            little_index = get_little_index(x, y)
            vertical[y].add(i)
            horizontal[x].add(i)
            little[little_index].add(i)

        def search(x, y):
            print(x, y)
            if x == 9:
                return True

            little_index = get_little_index(x, y)
            if board[x][y] == '.':
                for i in range(1, 9):
                    ii = str(i)
                    if ii not in vertical[y] and ii not in horizontal[x] and ii not in little[little_index]:
                        add(x, y, ii)

                        if y + 1 < 9:
                            find = search(x, y + 1)
                        else:
                            find = search(x + 1, 0)
                        if find:
                            return find

                        vertical[y].remove(ii)
                        horizontal[x].remove(ii)
                        little[little_index].remove(ii)
                        board[x][y] = '.'
                return False
            else:
                if y + 1 < 9:
                    return search(x, y + 1)
                else:
                    return search(x + 1, 0)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    add(i, j, board[i][j])

        search(0, 0)


