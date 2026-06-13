class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        s = x*(x+1)//2
        return s-sum(nums)