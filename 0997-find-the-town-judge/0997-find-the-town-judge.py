class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegr=[0]*(n+1)
        outde=[0]*(n+1)
        for a,b in trust:
            outde[a]+=1
            indegr[b]+=1
        for i in range(1,n+1):
            if indegr[i]==n-1 and outde[i]==0:
                return i
        return -1