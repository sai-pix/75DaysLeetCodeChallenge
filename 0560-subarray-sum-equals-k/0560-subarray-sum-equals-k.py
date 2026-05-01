class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        d={0:1}
        p_s=0
        for i in nums:
            p_s+=i
            if p_s-k in d:
                count+=d[p_s-k]
            d[p_s]=d.get(p_s,0)+1
        return count