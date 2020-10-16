from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for str in strs:
            time = [0] * 26
            for i in range(len(str)):
                time[ord(str[i]) - ord('a')] += 1

            temp = map.get(tuple(time), [])
            temp.append(str)
            map[tuple(time)] = temp

        ans = []
        for value in map.values():
            ans.append(value)
        return ans
