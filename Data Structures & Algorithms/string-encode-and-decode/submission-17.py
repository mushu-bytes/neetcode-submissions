class Solution:
    """
    Encode the list of strings by joining the strings based on a special delimiter?
    We then also need the length of each of the actual strings. Then can we use a 
    number to separate each string? Essentially the number would say: the next
    x characters form the next item in the string?
    But what if you have strings of multiple length?
    """
    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # find length of next string
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1

            length = int(length)
            start = j + 1
            end = start + length
            res.append(s[start: end])
            i = end

        return res





