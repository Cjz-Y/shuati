from typing import List


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []

        target = {}
        for item in p:
            target[item] = target.get(item, 0) + 1

        cur = {}
        cur_str = s[0:len(p)]
        for item in cur_str:
            cur[item] = cur.get(item, 0) + 1

        # print(cur)

        match = True
        for key, value in target.items():
            if value != cur.get(key, 0):
                match = False
                break

        if match:
            ans.append(0)

        for i in range(len(p), len(s)):
            cur[s[i - len(p)]] -= 1
            cur[s[i]] = cur.get(s[i], 0) + 1

            match = True
            for key, value in target.items():
                if value != cur.get(key, 0):
                    match = False
                    break
            if match:
                ans.append(i - len(p) + 1)

        return ans

