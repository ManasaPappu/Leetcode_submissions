class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Keep scanning left for the first position
                    else:
                        left = mid + 1   # Keep scanning right for the last position
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        # Execute modified binary search for both boundaries
        first_pos = findBound(isFirst=True)
        last_pos = findBound(isFirst=False)
        
        return [first_pos, last_pos]
