import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        max_heap  = []
        out       = 0
        box_count = 0 
        
        for box in boxTypes:
            heapq.heappush(max_heap, (-box[1], box[0]))
            
        while max_heap and box_count < truckSize:

            units_per_box, num_boxes = heapq.heappop(max_heap)
            
            for i in range(num_boxes):
                if box_count < truckSize:
                    out -= units_per_box
                    box_count += 1
                else:
                    break
        
        return out
            
            
            
        
        