#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
# 給一陣列cost, cost[i]代表在index i再走一次花費的成本, 每次可走1步或2步, return走到index n所花費的最小成本

# By DP and scrolling array, time: O(n), space: O(1)
# 就是用DP只是發現dp[i]只和dp[i-1]以及dp[i-2]有關, 所以迭代來省空間
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev = 0
        cur = 0
        for i in range(2, n+1):
            tmp = cur
            cur = min(cur+cost[i-1], prev+cost[i-2])
            prev = tmp
        return cur

# By DP, time: O(n), space: O(n)
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         # dp[i]代表走到index i 所花費得成本
#         dp = [0]*(n+1)
#         for i in range(2, n+1):
#             # 注意走到index i實際上不需要cost[i], 而是從index i-1或index i-2走1或2步過來
#             # 相對的走到index i-1或index i-2當下也不需要cost[i-1]和cost[i-2]
#             # 只是要從i-1或i-2走到i時, 需要再花費cost[i-1]和cost[i-2]才能走過來
#             dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
#         return dp[n]
        
# @lc code=end

