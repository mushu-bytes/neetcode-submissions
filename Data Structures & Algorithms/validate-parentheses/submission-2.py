class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(map[c])
            else:
                if stack == [] or stack.pop() != c:
                    return False

        return stack == []