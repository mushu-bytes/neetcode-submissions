class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValid(p1):
            x, y = p1
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        def backtrack(p1, count):
            x, y = p1
            if not isValid(p1):
                return False
            if board[x][y] != word[count]:
                return False
            seen.add(p1)
            if count == len(word) - 1:
                return True
            
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for n in neighbors:
                if n not in seen and backtrack(n, count + 1):
                    return True
            seen.remove(p1)
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if backtrack((i, j), 0):
                    return True

        return False

