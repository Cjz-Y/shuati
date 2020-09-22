from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def back(result, index, num):
            print(result, index, num)
            if index == len(s):
                return
            if num == 3:
                last = s[index:]
                if int(last) > 255 or (len(last) > 1 and last.startswith('0')):
                    return
                else:
                    result.append(last)
                    ans.append('.'.join(result))
                    result.pop()
                return

            for i in range(1, 4):
                if index + i >= len(s):
                    break

                item = s[index:index + i]
                if not (int(item) > 255 or (len(item) > 1 and item.startswith('0'))):
                    result.append(item)
                    back(result, index + i, num + 1)
                    result.pop()
                else:
                    break

        ans = []
        back([], 0, 0)

        return ans

if __name__ == '__main__':
    s = '1111'

    print(Solution().restoreIpAddresses(s))