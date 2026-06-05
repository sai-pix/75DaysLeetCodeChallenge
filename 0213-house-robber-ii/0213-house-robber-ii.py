class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def max_rob(arr):
            p1,p2=0,0
            for i in arr:
                p2,p1=p1,max(p1,p2+i)
            return p1
        return max(max_rob(nums[1:]),max_rob(nums[:-1]))