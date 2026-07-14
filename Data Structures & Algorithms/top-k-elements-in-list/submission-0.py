from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        res = []
        count = Counter(nums)
        print(count)

        for key, v in count.items():
            print(min_heap)
            heappush(min_heap, (v, key))
            if len(min_heap) > k:
                _ = heappop(min_heap)

        print(len(min_heap))
        while min_heap:
            v, key = heappop(min_heap)
            res.append(key)
        return res