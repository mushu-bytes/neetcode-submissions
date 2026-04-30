class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        combo = []
        def backtrack(i):
            if i == len(digits):
                res.append("".join(combo))
                return

            for letter in map[digits[i]]:
                combo.append(letter)
                backtrack(i + 1)
                combo.pop()
            
            return

        backtrack(0)
        if not digits:
            return []
        return res







