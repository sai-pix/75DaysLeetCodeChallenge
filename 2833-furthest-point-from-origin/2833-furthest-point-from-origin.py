class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left=moves.count('L')
        right=moves.count('R')
        distance=abs(left-right)+moves.count('_')
        return distance