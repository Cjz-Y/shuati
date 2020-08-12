from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            exist_x = set()
            exist_y = set()
            for j in range(len(board[i])):
                x = board[i][j]
                y = board[j][i]
                if x.isdecimal():
                    if x in exist_x:
                        return False
                    else:
                        exist_x.add(x)

                if y.isdecimal():
                    if y in exist_y:
                        return False
                    else:
                        exist_y.add(y)


        for i in range(3):
            for j in range(3):

                exist = set()
                for x in range(i * 3, (i + 1) * 3):
                    for y in range(j * 3, (j + 1) * 3):
                        temp = board[x][y]
                        if temp.isdecimal():
                            if temp in exist:
                                return False
                            else:
                                exist.add(temp)


        return True

