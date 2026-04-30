class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(lambda: 0)
        for letter in s:
            map[letter] += 1
        
        map2 = defaultdict(lambda: 0)
        for letter in t:
            map2[letter] += 1

        return map == map2
