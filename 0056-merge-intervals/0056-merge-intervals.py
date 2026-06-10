class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        re = [intervals[0]]
        for start,end in intervals[1:]:
            if re[-1][1] >= start:
                re[-1][1] = max(re[-1][1],end)
            else:
                re.append([start,end])

        return re