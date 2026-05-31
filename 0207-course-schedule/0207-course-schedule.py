class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        state=[0]*numCourses
        for c,p in prerequisites:
            graph[c].append(p)
        def dfs(c):
            if state[c]==1:
                return False
            if state[c]==2:
                return True
            state[c]=1
            for i in graph[c]:
                if not dfs(i):
                    return False
            state[c]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True