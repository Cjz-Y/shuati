from typing import List


class Solution:

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        由于每个节点之间距离都是1，所以离某一个1最近的0一定是直上直下的
        所以暴力四重奏
        :param matrix:
        :return:
        """
        ans = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    temp.append(0)
                else:
                    temp.append(999999)
            ans.append(temp)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    if i > 0:
                        ans[i][j] = min(ans[i - 1][j] + 1, ans[i][j])
                    if j > 0:
                        ans[i][j] = min(ans[i][j - 1] + 1, ans[i][j])

        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - 1, -1, -1):
                if matrix[i][j] == 1:
                    if i > 0:
                        ans[i][j] = min(ans[i - 1][j] + 1, ans[i][j])
                    if j < len(matrix[i]) - 1:
                        ans[i][j] = min(ans[i][j + 1] + 1, ans[i][j])

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    if i < len(matrix) - 1:
                        ans[i][j] = min(ans[i + 1][j] + 1, ans[i][j])
                    if j > 0:
                        ans[i][j] = min(ans[i][j - 1] + 1, ans[i][j])

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[i]) - 1, -1, -1):
                if matrix[i][j] == 1:
                    if i < len(matrix) - 1:
                        ans[i][j] = min(ans[i + 1][j] + 1, ans[i][j])
                    if j < len(matrix[i]) - 1:
                        ans[i][j] = min(ans[i][j + 1] + 1, ans[i][j])

        return ans




    def updateMatrix1(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        暴力方法 超时  可以优化  
        :param matrix:
        :return:
        """
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
            ans.append(temp)

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



