class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxf = res = 0
        mp = defaultdict(int)
        for r in range(len(s)):
            mp[s[r]] += 1
            maxf = max(maxf, mp[s[r]])
            while (r - l + 1) - maxf > k:
                mp[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)

        return res