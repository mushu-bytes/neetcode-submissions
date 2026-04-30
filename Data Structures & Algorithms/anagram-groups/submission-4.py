class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # tuple -> List[List[str]]

        def str_to_count(s: str):
            count = [0 for i in range(26)]
            for l in s:
                count[ord(l) - ord('a')] += 1
                
            return tuple(count)

        for s in strs:
            count = str_to_count(s)
            if count in anagrams:
                anagrams[count].append(s)
            else:
                anagrams[count] = [s]
        
        return list(anagrams.values())
