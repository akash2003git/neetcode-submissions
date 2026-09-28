class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        countT = defaultdict(int)
        for i in range(len(t)):
            countT [t[i]] += 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        window = defaultdict(int)

        l = 0
        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] += 1
                if window[s[r]] == countT[s[r]]:
                    have += 1
                
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                if s[l] in countT:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if not resLen == float("inf") else ""