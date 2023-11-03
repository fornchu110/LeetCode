#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start

#By DP
#�򥻷Q�kn���u����إi��:�t�@���ɸ�1�B�M�t�ⶥ�ɸ�2�B
#�ҥH���Pf(n) = f(n-1)+f(n-2)
#���]n = 5, ���׵��P��3������k��+��4������k��
class Solution:
    def climbStairs(self, n: int) -> int:
        p = 0
        q = 0
        r = 1
        for i in range(n):
            p = q
            q = r
            r = p+q
        return r

# @lc code=end

