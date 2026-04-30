class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long=0
        nums=(set(nums))
        for i in nums:
            if i-1 not in nums:
                curr=i
                count=1
                while curr+1 in nums:
                    curr+=1
                    count+=1
                long=max(count,long)
        return long