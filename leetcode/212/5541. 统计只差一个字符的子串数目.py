class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        f = {}

        for length in range(1, len(t) + 1):
            for start in range(len(t) - length + 1):
                end = start + length
                temp = t[start : end]
                f[temp] = f.get(temp, 0) + 1

                temp_arr = list(temp)
                for i in range(len(temp_arr)):
                    temp_arr[i] = '?'
                    temp_str = ''.join(temp_arr)
                    f[temp_str] = f.get(temp_str, 0) + 1
                    temp_arr[i] = temp[i]

        ans = 0
        for length in range(1, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length
                temp = s[start:end]

                temp_arr = list(temp)

                for i in range(len(temp_arr)):
                    temp_arr[i] = "?"
                    temp_str = ''.join(temp_arr)
                    ans += f.get(temp_str, 0) - f.get(temp, 0)
                    temp_arr[i] = temp[i]
        return ans

