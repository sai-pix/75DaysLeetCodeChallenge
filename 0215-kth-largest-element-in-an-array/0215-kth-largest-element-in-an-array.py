import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot=random.choice(nums)
        left=[x for x in nums if x>pivot]
        mid=[x for x in nums if x==pivot]
        right=[x for x in nums if x<pivot]
        if k<=len(left):
            return self.findKthLargest(left,k)
        elif k<=len(left)+len(mid):
            return pivot
        else:
            return self.findKthLargest(right,k-len(left)-len(mid))