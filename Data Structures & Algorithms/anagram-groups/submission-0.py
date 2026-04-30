class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # charCount -> string
        for s in strs:
            count = [0] * 26 # char -> count
            for c in s:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            if count in anagrams:
                anagrams[count].append(s)
            else:
                anagrams[count] = [s]
        return anagrams.values()
            