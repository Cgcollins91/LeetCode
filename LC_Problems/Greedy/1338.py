from collections import Counter
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        target           = len(arr) // 2
        num_counts       = Counter(arr)
        cumulative_count = 0 
        ans              = 0
        max_heap         = []
        
        for count in num_counts.values():
            heapq.heappush(max_heap, -count)
            
        while cumulative_count < target:
            cumulative_count +=  -heapq.heappop(max_heap)
            ans += 1
                
        
        return ans
            
            
        