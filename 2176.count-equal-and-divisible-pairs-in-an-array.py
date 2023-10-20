#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        idx, sort = sorted(zip(range(len(nums)), nums))
        print(idx, sort)

        
# @lc code=end

