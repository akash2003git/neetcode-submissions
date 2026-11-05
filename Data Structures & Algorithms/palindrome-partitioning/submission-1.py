class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []

        def backtrack(i):
            if i >= len(s):
                res.append(parts.copy())
                return 
            
            for j in range(i, len(s)):
                if self.is_palindrome(i, j, s):
                    parts.append(s[i:j+1])
                    backtrack(j + 1)
                    parts.pop()
        
        backtrack(0)

        return res

    def is_palindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True