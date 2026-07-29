class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}

        for i in s:
            count = hash_map_s.get(i)
            if count:
                hash_map_s[i] += 1
            else:
                hash_map_s[i] = 1
        for i in t:
            count = hash_map_t.get(i)
            if count:
                hash_map_t[i] += 1
            else:
                hash_map_t[i] = 1

        return hash_map_s == hash_map_t