class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:

        if K >= 2:
            min_arr = list(S)
            min_arr.sort()
            min_ans = "".join(min_arr)
            return min_ans
        else:
            new_s = S + S[:len(S) - 1]
            ans = S
            for i in range(len(S)):
                temp = new_s[i : i + len(S)]
                ans = min(ans, temp)
            return ans

