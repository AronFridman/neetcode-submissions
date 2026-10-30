class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(str(len(string)))
            encoded.append('#')
            encoded.append(string)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0;
        while i < len(s):
            seperator = s.find('#',i)
            num = int(s[i:seperator])
            i = seperator + 1
            strs.append(s[i:i + num])
            i += num
        return strs