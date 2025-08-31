# %%

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        
        # Binary Search
        while left <= right:
            #print(left, right)
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid - 1
                
            elif nums[mid] < target:
                left = mid + 1

        # If the target is not found, the left pointer will be at the insertion point
        return left


array = [1, 3, 4 , 6, 8, 10, 15, 18, 20, 25, 45, 60]
target = 16

Solution().searchInsert(array, target)
# %%
