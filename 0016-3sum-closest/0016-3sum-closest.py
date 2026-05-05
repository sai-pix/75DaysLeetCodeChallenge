class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close=float('inf')
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if abs(s-target)<abs(close-target):
                    close=s
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    return s
        return close