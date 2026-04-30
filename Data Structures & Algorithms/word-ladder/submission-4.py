class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        res = 1
        visited = set()
        q = deque([beginWord])
        newq = deque()
        while q:
            curr = q.popleft()
            if curr == endWord:
                return res
            for word in wordList:
                if word not in visited and self.adjacent(curr, word):
                    newq.append(word)
                    visited.add(word)
            if not q:
                res += 1
                q = newq
                newq = deque()
        return 0

    def adjacent(self, w1, w2):
        diff = 0
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                diff += 1
            if diff > 1:
                return False
        return diff == 1
