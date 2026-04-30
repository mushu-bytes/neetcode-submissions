class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1, s2, s3 = " " + s1, " " + s2, " " + s3
        ROWS, COLS = len(s1), len(s2)
        if ROWS + COLS != len(s3) + 1:
            return False

        m, n = 0, 0
        S = [[0 for i in range(COLS)] for i in range(ROWS)]
        S[0][0] = 1

        for r in range(ROWS):
            for c in range(COLS):
                if s1[r] == s3[r + c]:
                    if c > 0 and S[r][c - 1]:
                        m += 1
                        S[r][c] = 1
                    elif r > 0 and S[r - 1][c]:
                        S[r][c] = 1
                        m += 1

                if s2[c] == s3[r + c]:
                    if r > 0 and S[r - 1][c]:
                        n += 1
                        S[r][c] = 1
                    elif c > 0 and S[r][c - 1]:
                        S[r][c] = 1
                        n += 1

        print(S, m, n)
        return True if S[ROWS - 1][COLS - 1] else False
