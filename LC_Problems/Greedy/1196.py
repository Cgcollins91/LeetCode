import heapq

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        # convert weight to min_heap 
        heapify(weight)
        ans = 0
        total_weight = 0
        
        while weight:
            apple = heapq.heappop(weight)
            
            if total_weight + apple <= 5000:
                total_weight += apple
                ans += 1
            else:
                break
        
        return ans
                
        
        