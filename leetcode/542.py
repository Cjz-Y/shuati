from typing import List


class Solution:

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        ans = []
        zeros = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    temp.append(0)
                    zeros.append((i,j))
                else:
                    temp.append(999999)

        for x, y in zeros:
            cur = [(x, y)]
            next = []
            step = 1
            while cur:
                for child_x, child_y in cur:
                    if child_x > 0 and matrix[child_x - 1][child_y] == 1 and step < ans[child_x - 1][child_y]:
                        next.append((child_x - 1, child_y))
                        ans[child_x - 1][child_y] = step

                    if child_x < len(matrix) - 1 and matrix[child_x + 1][child_y] == 1 and step < ans[child_x + 1][child_y]:
                        next.append((child_x + 1, child_y))
                        ans[child_x + 1][child_y] = step

                    if child_y > 0 and matrix[child_x][child_y - 1] == 1 and step < ans[child_x][child_y - 1]:
                        next.append((child_x, child_y - 1))
                        ans[child_x][child_y - 1] = step

                    if child_y < len(matrix[child_x]) - 1 and matrix[child_x][child_y + 1] == 1 and step < ans[child_x][child_y + 1]:
                        next.append((child_x, child_y + 1))
                        ans[child_x][child_y + 1] = step

                cur = next
                next = []
                step = step + 1

        return ans

        # ans = []
        # ones = []
        # for i in range(len(matrix)):
        #     temp = []
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == 1:
        #             temp.append(99999)
        #             ones.append((i, j))
        #         else:
        #             temp.append(0)
        #
        #     ans.append(temp)
        #
        # for x,y in ones:
        #     result  = 99999
        #     cur = [(x,y)]
        #     next = []
        #     while cur:
        #         for child_x, child_y in cur:


