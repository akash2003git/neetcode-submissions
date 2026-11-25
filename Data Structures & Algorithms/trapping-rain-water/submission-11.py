class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)

        maxL = []
        maxi = 0
        for i in range(0, len(height)):
            maxL.append(maxi)
            maxi = max(maxi, height[i])

        maxR = [0] * n
        maxi = 0
        for i in range(n - 1, -1, -1):
            maxR[i] = maxi
            maxi = max(maxi, height[i])

        for i in range(len(height)):
            res += max(0, min(maxL[i], maxR[i]) - height[i])

        return res
