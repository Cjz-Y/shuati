import collections


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        pos = collections.defaultdict(list)
        null = 99999

        for i in range(len(ring)):
            pos[ring[i]].append(i)

        f = [[null for i in range(len(ring))] for j in range(len(key))]

        ans = null
        for i in range(len(key)):
            if i == 0:
                for j in range(len(pos[key[i]])):
                    current_pos = pos[key[i]][j]
                    # print(current_pos)
                    f[i][current_pos] = min([current_pos, len(ring) - current_pos])
            else:
                for j in range(len(pos[key[i]])):
                    current_pos = pos[key[i]][j]
                    for k in range(len(pos[key[i - 1]])):
                        pre_pos = pos[key[i - 1]][k]
                        if current_pos > pre_pos:
                            temp_value = min([current_pos - pre_pos, pre_pos + len(ring) - current_pos])
                        else:
                            temp_value = min([pre_pos - current_pos, current_pos + len(ring) - pre_pos])
                        f[i][current_pos] = min(f[i][current_pos], f[i - 1][pre_pos] + temp_value)

                        if i == len(key) - 1:
                            ans = min([ans, f[i][current_pos]])

        return ans + len(key)




