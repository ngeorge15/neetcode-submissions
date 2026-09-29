import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        pq = []
        for i, v in counts.items():
            heapq.heappush(pq, (-v, i))
        result = []

        for i in range(0, k):
            p, v = heapq.heappop(pq)
            result.append(v)

        return result
        
        