class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1, text2 = " " + text1, " " + text2
        ROWS, COLS = len(text1), len(text2)
        DP = [[0 for i in range(COLS)] for i in range(ROWS)]

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if text1[r] == text2[c]:
                    DP[r][c] = max(1 + DP[r - 1][c - 1], DP[r - 1][c], DP[r][c - 1])
                else:
                    DP[r][c] = max(DP[r - 1][c], DP[r][c - 1])
        return DP[ROWS - 1][COLS - 1]



