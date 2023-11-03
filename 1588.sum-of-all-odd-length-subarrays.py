#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
# By prefixsum(DP?), time: O(n^2), space: O(n)
# 還沒看懂, 這題還有數學解法
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)
        prefixSums = [0]*(n+1)
        for idx, i in enumerate(arr):
            prefixSums[idx+1] = prefixSums[idx]+i
        for start in range(n):
            length = 1
            while start+length<=n:
                end = start+length-1
                sum += prefixSums[end+1] - prefixSums[start]
                length += 2
        return sum
        
# @lc code=end

