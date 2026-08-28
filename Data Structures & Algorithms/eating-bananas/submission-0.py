class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            speed = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / speed)
        
            if totalTime <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        
        return res      