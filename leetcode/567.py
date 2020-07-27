class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        for item in s1:
            target[item] = target.get(item, 0) + 1

        cur = {}
        cur_str = s2[0:len(s1)]
        for item in cur_str:
            cur[item] = cur.get(item, 0) + 1

        # print(cur)

        match = True
        for key, value in target.items():
            if value != cur.get(key, 0):
                match = False
                break

        if match:
            return True


        for i in range(len(s1), len(s2)):
            cur[s2[i - len(s1)]] -= 1
            cur[s2[i]] = cur.get(s2[i], 0) + 1

            match = True
            for key, value in target.items():
                if value != cur.get(key, 0):
                    match = False
                    break
            if match:
                return True

        return False




    def checkInclusion222(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        print(len(s1))
        index = 0
        while index < len(s2):
            print('len s2 = %d, index = %d' % (len(s2), index))
            while index < len(s2) and s2[index] not in s1:
                # print('len s2 = %d, index = %d' % (len(s2), index))
                index += 1
            print("start index = %d" % index)
            process = s1
            left = index
            while index < len(s2) and (s2[index] in process or (s2[index] in s1 and s2[index] == s2[left])) and len(process) != 0:
                if s2[index] in process:
                    process = process.replace(s2[index], '', 1)
                elif s2[index] in s1 and s2[index] == s2[left]:
                    left += 1
                index += 1

            print('end index = %d, len process = %d' % (index, len(process)))

            if len(process) == 0:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    a = "adc"
    b = "dcda"
    print(s.checkInclusion(a,b))