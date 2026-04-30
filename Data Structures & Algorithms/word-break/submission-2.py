class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Off the bat this looks like coin change but with words
        This will be a boolean 1-D problem

        The problem that I am forseeing is knowing when to break a word,
        If we break a word once, that means we gain another break point
        Do we keep track of all break points?

        I don't think so, since our solution to inefficient. When can
        we give up a break point?


        """
        words = set(wordDict)
        breakpoints = [0]
        dp = [False] * (len(s) + 1)
        for i in range(len(s) + 1):
            for bp in breakpoints:
                if s[bp:i + 1] in words:
                    dp[i] = True
                    breakpoints.append(i + 1)
                    break

        return dp[len(s)]
                