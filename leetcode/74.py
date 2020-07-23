from typing import List


class Solution:

    def search(self, matrix, left, right, target):

        mid = int((left + right) / 2)
        # print('left = %d, right = %d, mid = %d' % (left, right, mid))
        if left == right:
            if matrix[mid][0] <= target:
                return left
            else:
                return left - 1

        if matrix[mid][0] < target:
            return self.search(matrix, mid + 1, right, target)
        else:
            return self.search(matrix, left, mid, target)

    def search2(self, num, left, right, target):
        # print('left = %d, right = %d' % (left, right))
        mid = int((left + right) / 2)
        if target == num[mid]:
            return mid

        if left == right and target != num[mid]:
            return -1

        if target > num[mid]:
            return self.search2(num, mid + 1, right, target)
        else:
            return self.search2(num, left, mid, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        index = self.search(matrix, 0, len(matrix) - 1, target)
        # print('index = %d' % index)
        if index == -1:
            return False

        index = self.search2(matrix[index], 0, len(matrix[index]) - 1, target)
        # print('index = %d' % index)
        if index == -1:
            return False
        else:
            return True


