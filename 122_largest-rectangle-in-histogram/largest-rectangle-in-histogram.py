class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        # write your code here
        if not heights:
            return 0
            
        res = 0
        stack = []
        # [2, 1, 5, 6, 2]
        for i in range(len(heights)):
            cur = -1 if i == len(heights) - 1 else heights[i]
            while stack and heights[stack[-1]] >= cur:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                res = max(res, width * height)
            stack.append(i)
        return res
