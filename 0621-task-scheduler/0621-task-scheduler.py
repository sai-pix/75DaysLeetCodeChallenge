from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)

        maxFreq = max(count.values())

        countMax = 0

        for v in count.values():
            if v == maxFreq:
                countMax += 1

        ans = (maxFreq - 1) * (n + 1) + countMax

        return max(ans, len(tasks))