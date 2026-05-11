class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            stack=[]
            while i!=0:
                n=i%10
                i//=10
                stack.append(n)
            while stack:
                ans.append(stack.pop())
        return ans