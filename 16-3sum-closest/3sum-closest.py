class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()

        closest_sum = nums[0] + nums[1] + nums[2]

        for fixed in range(len(nums) - 2):
            left = fixed + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[fixed] + nums[left] + nums[right]

                
                if current_sum == target:
                    return current_sum

            
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum