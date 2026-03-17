class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        heap=[]
        for n,c in freq.items():
            heapq.heappush(heap,(-c,n))
        result=[]
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result