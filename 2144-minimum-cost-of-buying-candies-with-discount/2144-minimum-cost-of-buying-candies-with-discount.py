class Solution:
    def minimumCost(self, cost: List[int]) -> int:
       s=0
       if len(cost)<=2:
        return s+sum(cost)
       cost.sort()
       
       while len(cost)>2:
        x=cost.pop()
        y=cost.pop()
        s+=x+y
        cost.pop()
       return s+sum(cost)