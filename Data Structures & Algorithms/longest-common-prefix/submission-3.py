class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        curr_idx = 0
        curr_str = ""
        curr_ltr = ""
        while True: 
            if curr_idx >= len(strs[0]):
                return curr_str
            curr_ltr = strs[0][curr_idx]
            for s in strs:
                if curr_idx >= len(s) or s[curr_idx] != curr_ltr:
                    return curr_str
            curr_str += curr_ltr
            curr_idx += 1
        return curr_str
