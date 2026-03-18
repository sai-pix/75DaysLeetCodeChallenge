class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left,right=1,1
        n=len(nums)
        result=[1]*n
        for i in range(n):
            result[i]=left
            left*=nums[i]
        for i in range(n-1,-1,-1):
            result[i]*=right
            right*=nums[i]
        return result