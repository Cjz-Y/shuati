from typing import List


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        null = 9999999

        pre_fir_min, pre_sec_min = 0, 0
        pre_fir_min_index, pre_sec_min_index = -1, -1

        for i in range(len(arr)):
            cur_fir_min, cur_sec_min = null, null
            cur_fir_min_index, cur_sec_min_index = -1, -1
            for j in range(len(arr[i])):
                if j != pre_fir_min_index:
                    temp = pre_fir_min + arr[i][j]
                else:
                    temp = pre_sec_min + arr[i][j]
                if temp < cur_fir_min:
                    if cur_fir_min < cur_sec_min:
                        cur_sec_min = cur_fir_min
                        cur_sec_min_index = cur_fir_min_index
                    cur_fir_min = temp
                    cur_fir_min_index = j
                elif temp < cur_sec_min:
                    cur_sec_min = temp
                    cur_sec_min_index = j
            pre_fir_min, pre_sec_min = cur_fir_min, cur_sec_min
            pre_fir_min_index, pre_sec_min_index = cur_fir_min_index, cur_sec_min_index

        return cur_fir_min
