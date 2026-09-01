class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0] * 26

        for ch in s1:
            count[ord(ch) - ord('a')] += 1

        for l in range(len(s2) - len(s1) + 1):
            r = l + len(s1)

            ref = count.copy()

            for ch in s2[l:r]:
                ref[ord(ch) - ord('a')] -= 1

            if all(c == 0 for c in ref):
                return True

        return False