class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = " " + word1
        w2 = " " + word2
        size = max(len(w1), len(w2))
        for i in range(len(word1), size):
            w1 += " "
        for j in range(len(word2), size):
            w2 += " "

        D = [[0 for i in range(size)] for i in range(size)]
        for i in range(size):
            D[i][0] = i
            D[0][i] = i

        for i in range(size):
            for j in range(size):
                if i > 0 and j > 0:
                    D[i][j] += min(
                        1 + D[i][j - 1],
                        1 + D[i - 1][j],
                        1 + D[i - 1][j - 1] if w1[i] != w2[j] else D[i - 1][j - 1]
                    )
        return D[len(word1)][len(word2)]