class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        n1=len(s1)
        n2=len(s2)
        if n2<n1:
            return False
        c=Counter(s1)
        win=Counter(s2[:n1])
        if c==win:
            return True
        for i in range(n1,n2):
            win[s2[i]]+=1
            win[s2[i-n1]]-=1
            if win[s2[i-n1]]==0:
                del win[s2[i-n1]]
            if win==c:
                return True
        return False