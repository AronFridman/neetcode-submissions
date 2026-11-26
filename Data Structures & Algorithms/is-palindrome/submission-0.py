class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        newString = [c for c in s if c.isalnum()]
        s = "".join(newString)

        reversed = s[::-1]

        if reversed.lower() == s.lower():
            return True
        return False