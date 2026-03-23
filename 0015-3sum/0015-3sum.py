class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        r = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            x,y=i+1,len(nums)-1
            while x<y:
                if nums[i]+nums[x]+nums[y] == 0:
                    r.append([nums[i],nums[x],nums[y]])
                    x+=1
                    y-=1
                    while x<y and nums[x]==nums[x-1]:
                        x+=1
                    while x<y and nums[y]==nums[y+1]:
                        y-=1
                elif nums[i]+nums[x]+nums[y]<0:
                    x+=1
                else:
                    y-=1
        return r