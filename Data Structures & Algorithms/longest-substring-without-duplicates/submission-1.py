class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        l = 0
        r = 0
        longestString = set()
        while r < len(s):
            if s[r] not in longestString:
                longestString.add(s[r])
            else:
                longestString.remove(s[l])
                l+=1
                while s[r] in longestString:
                    longestString.remove(s[l])
                    l+=1
                longestString.add(s[r])
            r+=1
            output = max(output, len(longestString))
        return output

