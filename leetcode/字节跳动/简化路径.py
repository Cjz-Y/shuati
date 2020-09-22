class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')

        stack = []

        for cur in l:
            if cur == '':
                continue
            elif cur == '.':
                continue
            elif cur == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(cur)
        return '/' + '/'.join(stack)