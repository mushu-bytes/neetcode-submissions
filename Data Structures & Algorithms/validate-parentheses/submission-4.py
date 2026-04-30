class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []

        for b in s:
            if b in brackets:
                stack.append(brackets[b])
            else:
                if not stack or b != stack.pop():
                    return False
        
        return stack == []