class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Binary Search is usually used on sorted arrays and runs in O(logn) time complexity to return the index of a target
        # In each iteration, we half the search area. 
        # We use a left pointer and a right pointer to define the the bounds of the current search area within the array
        # We calculate the midpoint between the left and right pointers each iteration
        # If the target is > than the current midpoint, we move the right pointer to the left of mid by 1 index 
        # If the target is < than the current midpoint, we move the left pointer to the right of mid by 1 index
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return -1

