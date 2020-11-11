from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        f = [False for i in range(len(arr))]

        for i in range(len(arr)):
            for j in range(len(pieces)):
                if i - len(pieces[j]) == -1 or (i - len(pieces[j]) >= 0 and f[i - len(pieces[j])]):
                    index = i - len(pieces[j]) + 1
                    flag = True
                    for k in range(len(pieces[j])):
                        if pieces[j][k] != arr[index]:
                            flag = False
                            break
                    if flag:
                        f[i] = True
                        break
                if f[i]:
                    break
        return f[len(arr) - 1]