class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        count_s = {}
        count_t = {}
        for char in s:
            count_s[char] = count_s.get(char,0) + 1
        for char in t:
            if char not in count_s:
                return False
            count_t[char] = count_t.get(char,0) + 1
        for char in s:
            if count_s.get(char) != count_t.get(char):
                return False
        return True
            