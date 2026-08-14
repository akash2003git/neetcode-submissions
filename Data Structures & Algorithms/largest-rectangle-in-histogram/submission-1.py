class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[pair(startIndex, height)]
        maxArea = 0

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                startIndex = index
            stack.append((startIndex, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea