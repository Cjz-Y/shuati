from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        counter = Counter(words)

        for key, value in counter.items():
            counter[key] = -value

        m = len(words[0])

        length = m * len(words)

        words = set(words)

        ans = []

        for start in range(m):
            tail = start + length
            child = s[start:tail]
            child_counter = counter.copy()
            # print('start')
            # print(child_counter)

            # 先统计第一个长度的所有子字符串
            for i in range(len(child)):
                child_str = child[i * m: (i + 1) * m]
                if child_str in words:
                    child_counter[child_str] = child_counter.get(child_str, 0) + 1
                    if child_counter[child_str] == 0:
                        child_counter.pop(child_str)

            if len(child_counter) == 0:
                ans.append(start)

            # print(child_counter)
            # print(child_counter)

            while tail + m <= len(s):
                # 减去前面的前缀
                # print('start = %d' % start)

                child_str = s[start:start + m]
                # print('pre = %s' % child_str)
                if child_str in words:
                    child_counter[child_str] = child_counter.get(child_str, 0) - 1
                    if child_counter[child_str] == 0:
                        child_counter.pop(child_str)

                # 加上后缀
                child_str = s[tail:tail + m]
                # print('after = %s' % child_str)
                if child_str in words:
                    child_counter[child_str] = child_counter.get(child_str, 0) + 1
                    if child_counter[child_str] == 0:
                        child_counter.pop(child_str)

                # print(child_counter)

                start += m
                tail += m

                if len(child_counter) == 0:
                    ans.append(start)

        ans.sort()
        return ans




