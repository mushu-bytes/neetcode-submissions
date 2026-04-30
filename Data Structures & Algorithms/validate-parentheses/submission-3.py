class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for c in s:
            if c in map:
                stack.append(map[c])
            else:
                if stack == [] or stack.pop() != c:
                    return False

        return stack == []