class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for i in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if (val:=board[i][j])=='.':
                    continue
                b_i=(i//3)*3+j//3
                if val in row[i] or val in cols[j] or val in box[b_i]:
                    return False
                row[i].add(val)
                cols[j].add(val)
                box[b_i].add(val)
        return True