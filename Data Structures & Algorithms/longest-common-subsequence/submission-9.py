class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text2), len(text1)
        DP = [[0 for i in range(COLS)] for i in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if text1[c] == text2[r]:
                    if r - 1 >= 0 and c - 1 >= 0:
                        DP[r][c] = DP[r - 1][c - 1]
                    DP[r][c] += 1
                else:
                    DP[r][c] = max(DP[r - 1][c], DP[r][c - 1])
        return DP[ROWS-1][COLS-1]


