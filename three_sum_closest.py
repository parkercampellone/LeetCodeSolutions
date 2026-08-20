"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4


WOW I got this problem done in like 1 hour! this is great!!! I just had to figure out under what condition to move which pointer and that was easy from there!
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = nums[0] + nums[1] + nums[2]
        distance_from_target = 10000
        nums.sort()

        for i in range(len(nums)):
            fixed_val = nums[i]
            left = i + 1
            right = (len(nums) -1)

            while left < right:

                left_val = nums[left]
                right_val = nums[right]

                triplet = fixed_val + left_val + right_val

                dist = abs(triplet - target)

                if dist < distance_from_target:
                    answer = triplet
                    distance_from_target = dist

                if triplet > target:
                    right -= 1

                elif triplet <= target:
                    left += 1

                    
        return answer
                
                
