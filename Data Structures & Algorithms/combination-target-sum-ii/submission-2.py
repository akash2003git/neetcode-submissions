class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub_set = []

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(sub_set.copy())
                return
            if i > len(candidates) - 1 or remaining < 0:
                return
 
            sub_set.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i])
            sub_set.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, remaining)

        backtrack(0, target)
        return res 