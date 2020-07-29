from typing import List


class Solution:
    ans = []
    def back(self, pos, cur, s, result):
        if cur == 4:
            temp = s[pos:]
            if (s[pos] == '0' and len(temp) > 1) or int(temp) > 255:
                return
            self.ans.append(result + temp)
            return

        if s[pos] == '0':
            range_end = 2
        else:
            range_end = 4
        for length in range(1, range_end):
            end = pos + length - 1
            if len(s) - 1 - end > (4 - cur) * 3:
                continue
            if len(s) - 1 - end < 4 - cur:
                break
            if int(s[pos:end+1]) > 255:
                break

            self.back(end + 1, cur + 1, s, result + s[pos:end+1] + '.')

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        self.ans = []
        self.back(0, 1, s, "")
        return self.ans

if __name__ == '__main__':
    s = Solution()
    a = "172162541"

    print(s.restoreIpAddresses(a))