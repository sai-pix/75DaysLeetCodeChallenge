class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[0]+heights+[0]
        stack=[]
        area=0
        for i,h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                height=heights[stack.pop()]
                width=i-stack[-1]-1
                area=max(area,height*width)
            stack.append(i)
        return area