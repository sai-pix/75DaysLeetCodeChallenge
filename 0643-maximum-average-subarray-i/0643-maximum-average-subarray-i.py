class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumN=sum(nums[:k])
        max_Ave=sumN
        for i in range(k,len(nums)):
            sumN+=nums[i]
            sumN-=nums[i-k]
            max_Ave=max(sumN,max_Ave)
        return max_Ave/k
