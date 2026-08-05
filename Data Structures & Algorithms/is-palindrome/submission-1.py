class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitizedString = ""
        for c in s:
            if c.isalnum():
                sanitizedString += c.lower()

        i, j = 0, len(sanitizedString) - 1
        while i < j:
            if sanitizedString[i] != sanitizedString[j]:
                return False
            i += 1
            j -= 1

        return True