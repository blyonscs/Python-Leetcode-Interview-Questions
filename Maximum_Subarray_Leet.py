#Leetcode 53 Maximum Subarray, Given an Integer array nums, find the contiguous subarray (with at least one number) which has the largest sum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # input 1 -> 2 -> 4, 1 -> 3 -> 4, output 1 -> 1 -> 2 -> 3 -> 4 -> 4


class Solution:
    def  maxSubArray(self, nums: List[int]) -> int:
       maxSub = nums[0]
       curSum = 0

       for n in nums:
           if curSum < 0: # If curSum is negitive, it goes back to 0
               curSum = 0
           curSum += n
           maxSub = max(maxSub, curSum) #checking if curSum is the maxSum
       return maxSub
           
    #[4, -1, 2, -1] has the largest sum 6
    # linear time O(n)
    