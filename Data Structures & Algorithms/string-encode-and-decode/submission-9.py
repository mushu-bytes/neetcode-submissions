class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num_len = 1
            while s[i + num_len] != "#":
                num_len += 1

            count = int(s[i : i + num_len])
            res.append(s[i + num_len + 1: i + num_len + 1 + count])
            i += 1 + count + num_len
        return res


