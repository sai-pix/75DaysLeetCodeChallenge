class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        mA=0
        while left < right:
            area=min(height[left],height[right])*(right-left)
            mA=max(mA,area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return mA
