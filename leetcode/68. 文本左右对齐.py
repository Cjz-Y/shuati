from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        sum = 0
        temp = []
        ans = []
        for i in range(len(words)):
            word = words[i]
            if sum + len(word) + len(temp) <= maxWidth:
                temp.append(word)
                sum += len(word)
            else:
                unuse = maxWidth - sum
                link_ch = ' ' * (unuse // (len(temp) - 1)) if len(temp) > 1 else ' ' * unuse
                more = unuse % (len(temp) - 1) if len(temp) > 1 else 0
                for i in range(more):
                    temp[i] = temp[i] + ' '

                if len(temp) == 1:
                    temp.append('')

                ans.append(link_ch.join(temp))

                temp = [word]
                sum = len(word)

        ans.append(' '.join(temp) + (maxWidth - (len(temp) - 1) - sum) * ' ')
        return ans
