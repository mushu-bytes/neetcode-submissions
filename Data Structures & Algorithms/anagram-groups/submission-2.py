class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}
        for string in strs:
            counter = [0 for i in range(26)]
            for c in string:
                counter[ord(c) - ord("a")] += 1 
            if tuple(counter) in sublists:
                sublists[tuple(counter)].append(string)
            else:
                sublists[tuple(counter)] = [string]

        return list(sublists.values())