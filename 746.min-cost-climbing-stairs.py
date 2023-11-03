#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
# ���@�}�Ccost, cost[i]�N��bindex i�A���@����O������, �C���i��1�B��2�B, return����index n�Ҫ�O���̤p����

# By DP and scrolling array, time: O(n), space: O(1)
# �N�O��DP�u�O�o�{dp[i]�u�Mdp[i-1]�H��dp[i-2]����, �ҥH���N�Ӭ٪Ŷ�
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
#         # dp[i]�N����index i �Ҫ�O�o����
#         dp = [0]*(n+1)
#         for i in range(2, n+1):
#             # �`�N����index i��ڤW���ݭncost[i], �ӬO�qindex i-1��index i-2��1��2�B�L��
#             # �۹諸����index i-1��index i-2��U�]���ݭncost[i-1]�Mcost[i-2]
#             # �u�O�n�qi-1��i-2����i��, �ݭn�A��Ocost[i-1]�Mcost[i-2]�~�ਫ�L��
#             dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
#         return dp[n]
        
# @lc code=end

