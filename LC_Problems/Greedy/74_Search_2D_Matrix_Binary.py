class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols-1
        row         = 0

        while row < rows:
            left, right = 0, cols-1
            if target > matrix[row][cols-1]:
                row += 1

                if row > rows-1:
                    return False
                continue
            else:
                while left <= right:
                    
                    mid = (left + right) // 2

                    if matrix[row][mid] == target:
                        return True
                    
                    if matrix[row][mid] > target:
                        right = mid - 1

                    elif matrix[row][mid] < target:
                        left = mid + 1
                
                return False
        
        return False

                    