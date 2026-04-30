class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = " " + word1
        w2 = " " + word2
        ROWS, COLS = len(w1), len(w2)

        D = [[0 for i in range(COLS)] for i in range(ROWS)]
        for i in range(ROWS):
            D[i][0] = i
        for i in range(COLS):
            D[0][i] = i

        for i in range(ROWS):
            for j in range(COLS):
                if i > 0 and j > 0:
                    D[i][j] += min(
                        1 + D[i][j - 1],
                        1 + D[i - 1][j],
                        1 + D[i - 1][j - 1] if w1[i] != w2[j] else D[i - 1][j - 1]
                    )

        return D[len(word1)][len(word2)]