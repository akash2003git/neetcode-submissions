class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = float("-inf")
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxi = max(maxi, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxi
        

# 0 1 2 3 4 5 6 7
# 1 7 2 5 4 7 3 6