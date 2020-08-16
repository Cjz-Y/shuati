class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top == '(':
                    if item != ')':
                        return False
                elif top == '[':
                    if item != ']':
                        return False
                elif top == '{':
                    if item != '}':
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
