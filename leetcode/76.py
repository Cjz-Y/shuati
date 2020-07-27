class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # exist = {}
        windows = []
        winpos = []
        cur_s = t

        ans = 99999
        ans_start = -1
        ans_end = -1
        for i in range(len(s)):
            if s[i] in t:
                if s[i] not in cur_s:
                    for j in range(len(windows)):
                        if s[i] == windows[j]:
                            windows.remove(windows[j])
                            winpos.remove(winpos[j])
                            break
                    windows.append(s[i])
                    winpos.append(i)
                else:
                    cur_s = cur_s.replace(s[i], '', 1)
                    windows.append(s[i])
                    winpos.append(i)

                # if s[i] in exist.keys():
                #     pre_item_pos = exist.get(s[i])
                #     print('s[i] = %s, pre_pos = %d' % (s[i], pre_item_pos))
                #     windows.remove(windows[pre_item_pos])
                #
                # now_pos = len(windows)
                # exist[s[i]] = now_pos
                # windows.append(i)

                # print(windows)

                if len(windows) == len(t) and winpos[-1] - winpos[0] < ans:
                    ans = winpos[-1] - winpos[0]
                    ans_start = winpos[0]
                    ans_end = winpos[-1]

        if ans == 99999:
            return ""
        else:
            return s[ans_start : ans_end + 1]

if __name__ == '__main__':
    s = Solution()
    a = "ADOBECODEBANC"

    b = "ABC"
    print(s.minWindow(a, b))