class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""
            j = 0
            while s[i + j] != "#":
                length += s[i + j]
                j += 1
            length = int(length)
            res.append(s[i + j + 1: i + j + length + 1])
            i += 1 + length + j
        return res


