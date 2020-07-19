class Solution:
    def decodeString(self, s: str) -> str:

        times = []
        strings = []

        index = 0
        while index < len(s):
            if s[index] in '0123456789':
                integer = ''
                while s[index] in '0123456789':
                    integer = integer + s[index]
                    index = index + 1
                times.append(int(integer))

            elif s[index] == ']':
                string = ''
                item = strings.pop()
                while item != '[':
                    string = item + string
                    item = strings.pop()

                time = times.pop()
                strings.append(time * string)
                index = index + 1
            else:
                strings.append(s[index])
                index = index + 1

        return ''.join(strings)




