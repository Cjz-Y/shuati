class Solution:

    def binary_search(self, start, end, nums, target):

        mid = int((start + end) / 2)
        # print('start = %d, mid = %d, end = %d' % (start, mid, end))
        if mid == start:
            if nums[start] == target or nums[end] == target:
                return -1
            else:
                if target > nums[end]:
                    return end
                else:
                    return start

        if target == nums[mid]:
            return -1
        if target > nums[mid]:
            return self.binary_search(mid, end, nums, target)
        if target < nums[mid]:
            return self.binary_search(start, mid, nums, target)


    def search(self, start_x, start_y, end_x, end_y, matrix, target):
        result_y = self.binary_search(start_y, end_y, matrix[start_x], target)
        if result_y == -1:
            return True

        sample = [temp[start_y] for temp in matrix]

        result_x = self.binary_search(start_x, end_x, sample, target)
        if result_x == -1:
            return True

        # print('result_x = %d result_y = %d' % (result_x, result_y))

        if result_y != end_y or result_x != end_x:
            return self.search(start_x, start_y, result_x, result_y, matrix, target)
        else:
            result_y = self.binary_search(start_y, end_y, matrix[end_x], target)
            if result_y == -1:
                return True
            # print('len x = %d and len y = %d' % (len(matrix), len(matrix[0])))

            sample = [temp[end_y] for temp in matrix]
            result_x = self.binary_search(start_x, end_x, sample, target)
            if result_x == -1:
                return True

            # print('result_x2 = %d result_y2 = %d' % (result_x, result_y))

            if result_y == end_y or result_x == end_x:
                return False

            if (result_y != start_y or target > matrix[end_x][result_y]) or (result_x != start_x and target > matrix[result_x][end_y]):
                if result_y == start_y and target < matrix[end_x][result_y]:
                    result_y -= 1
                if result_x == start_x and target < matrix[result_x][end_y]:
                    result_x -= 1

                # print('result_x2 = %d result_y2 = %d' % (result_x, result_y))
                return self.search(result_x + 1, result_y + 1, end_x, end_y, matrix, target)
            else:
                return False



    def searchMatrix(self, matrix, target):
        """
        找第一行中比target大的 新的列数
        找第一列中比target大的 新的行数

        如果没有的话

        找最后一行比target小的 新的列数
        找最后一列比target小的 新的行数


        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        return self.search(0, 0, len(matrix) - 1, len(matrix[0]) - 1, matrix, target)



if __name__ == '__main__':
    a = [1,1]
    s = Solution()
    print(s.searchMatrix([a], 2))