from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(int(n / 2)):
            start = i
            end = n - i - 1
            for swap in range(start, end):
                reverse_swap = n - swap - 1
                print('start = %d, swap = %d, reverse_swap = %d, end = %d' % (start, swap, reverse_swap, end))
                matrix[start][swap], matrix[swap][end], matrix[end][reverse_swap], matrix[reverse_swap][start] = matrix[reverse_swap][start], matrix[start][swap], matrix[swap][end], matrix[end][reverse_swap]

                # temp = matrix[i][start]
                # matrix[i][start] = m

        for i in range(len(matrix)):
            print(matrix[i])

if __name__ == '__main__':
    a = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    solution = Solution()
    print(solution.rotate(a))