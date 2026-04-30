class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count: [strings with that count]
        counts = defaultdict(list)
        for s in strs:
            count = [0 for i in range(26)]
            for c in s:
                count[ord(c) - ord("a")] += 1
            counts[tuple(count)].append(s)
        
        return counts.values()
