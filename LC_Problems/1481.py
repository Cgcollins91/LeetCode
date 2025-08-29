from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        counts   = Counter(arr)
        num_int  = len(counts)
        min_heap = list(counts.values())
        heapq.heapify(min_heap)


        while min_heap:
            pop_cnt = heapq.heappop(min_heap)
            if pop_cnt <= k:
                k       -= pop_cnt
                num_int -= 1
            else:
                break

        return num_int
        


