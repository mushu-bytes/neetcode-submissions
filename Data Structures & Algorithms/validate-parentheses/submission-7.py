class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for c in s:
            if c in parens:
                stack.append(parens[c])
            else:
                if stack and c == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []