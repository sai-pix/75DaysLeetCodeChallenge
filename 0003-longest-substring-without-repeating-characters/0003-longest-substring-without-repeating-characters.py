class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch=set()
        left,max_length=0,0
        for right in range(len(s)):
            while s[right] in ch:
                ch.remove(s[left])
                left+=1
            ch.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length