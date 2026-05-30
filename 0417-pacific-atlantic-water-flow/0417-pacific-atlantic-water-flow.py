class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pasi,atl=set(),set()
        def dfs(r,c,vis):
            vis.add((r,c))
            dire=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in dire:
                nr,nc=r+dr,c+dc
                if(
                    0<=nr<rows 
                    and 0<=nc<cols and
                    (nr,nc) not in vis and
                    heights[nr][nc]>=heights[r][c]
                    ):
                    dfs(nr,nc,vis)
        for c in range(cols):
            dfs(0,c,pasi)
        for r in range(rows):
            dfs(r,0,pasi)
        for c in range(cols):
            dfs(rows-1,c,atl)
        for r in range(rows):
            dfs(r,cols-1,atl)
        return list(pasi & atl)