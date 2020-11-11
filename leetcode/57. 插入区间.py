from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        deal = False
        new_start, new_end = newInterval[0], newInterval[1]

        index = 0
        while index < len(intervals):
            # print('index = %d len = %d' % (index, len(intervals)))
            start, end = intervals[index][0], intervals[index][1]
            # print(start, end, new_start, new_end)

            # [1,3] [4,6]
            if end < new_start and end < new_end:
                index += 1
                continue
            # [1,3] [2,4]
            if start < new_start <=end < new_end:
                new_start = start
                new_end = new_end
                intervals.pop(index)
                continue

            # [1,4] [2,3], 不用管，原来就是答案
            if start <= new_start <= new_end <= end:
                deal = True
                break

            # [2,4] [1,3]
            if new_start < start <= new_end < end:
                intervals[index][0] = new_start
                intervals[index][1] = end
                deal = True
                break


            if new_start <= start <= end <= new_end:
                intervals.pop(index)
                continue

            # [4,6] [1,3]
            if new_end < start and new_end < end:
                intervals.insert(index, [new_start, new_end])
                deal = True
                break

        if not deal:
            intervals.append([new_start, new_end])
        return intervals

if __name__ == '__main__':
    a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    b = [4, 8]

    a = [[0, 0], [1, 4], [6, 8], [9, 11]]
    b = [0, 9]

    print(Solution().insert(a, b))
