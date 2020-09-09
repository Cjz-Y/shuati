from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        up_end, down_end, left_end, right_end = -1, len(matrix), -1, len(matrix[0])

        x_direct = [0, 1, 0, -1]
        y_direct = [1, 0, -1, 0]

        ans = [matrix[0][0]]

        x, y = 0, 0
        flag = True
        while flag:
            flag = False
            for i in range(4):

                while up_end < x + x_direct[i] < down_end and left_end < y + y_direct[i] < right_end:
                    flag = True
                    x += x_direct[i]
                    y += y_direct[i]
                    ans.append(matrix[x][y])

                if i == 0:
                    up_end += 1
                elif i == 1:
                    right_end -= 1
                elif i == 2:
                    down_end -= 1
                else:
                    left_end += 1

        return ans

