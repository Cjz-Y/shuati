class Solution:
    def reverseWords(self, s: str) -> str:

        l = s.split(' ')
        l = list(filter(lambda x: x != '', l))
        return ' '.join(reversed(l))



