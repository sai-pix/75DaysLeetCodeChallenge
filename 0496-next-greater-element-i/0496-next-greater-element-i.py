class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nge={}
        for n in nums2:
            while stack and n>stack[-1]:
                nge[stack.pop()]=n
            stack.append(n)
        while stack:
            nge[stack.pop()]=-1
        return [nge[n] for n in nums1]