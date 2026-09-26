class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        window, countT = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]

            if c in countT:
                window[c] = window.get(c, 0) + 1
                if window[c] == countT[c]:
                    have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                left = s[l]
                if left in countT:
                    window[left] -= 1
                    if window[left] < countT[left]:
                        have -= 1
                    
                l += 1

        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""