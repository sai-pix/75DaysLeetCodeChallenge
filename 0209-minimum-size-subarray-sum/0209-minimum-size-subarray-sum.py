class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ans=float('inf')
        s=0
        for right in range(len(nums)):
            s+=nums[right]
            while s>=target:
                ans=min(ans,right-left+1)
                s-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0