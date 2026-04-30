class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValid(p1, p2):
            x, y = p1
            x0, y0 = p2
            if x == x0 and y == y0:
                return False
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        def backtrack(p1, p2, count, seen):
            x, y = p1
            if not isValid(p1, p2):
                return False
            if board[x][y] != word[count]:
                return False
            seen.add(p1)
            if count == len(word) - 1:
                return True
            
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for n in neighbors:
                if n not in seen and backtrack(n, p1, count + 1, seen):
                    return True
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack((i, j), (-1, -1), 0, set()):
                    return True

        return False

