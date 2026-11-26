class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0
        l = 0
        r = 0 
        window = {}
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) +1
            maxFreq = max(window.values())
            windowLength = r-l + 1
            replacement =  windowLength - maxFreq
            while (r-l+1) - max(window.values()) > k:
                window[s[l]] -= 1
                l +=1
            output = max(output, r - l + 1)
            r+=1
        return output

