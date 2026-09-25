class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        bopen = '({['
        bclose = ']})'
        for ch in s:
            if ch in bopen:
                stack.append(ch)
            if ch in bclose:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if ch == ')' and curr != '(':
                    return False
                if ch == ']' and curr != '[':
                    return False
                if ch == '}' and curr != '{':
                    return False
        if len(stack) != 0:
            return False
        return True


        