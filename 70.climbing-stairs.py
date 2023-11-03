#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start

#By DP
#基本想法n階只有兩種可能:差一階時跨1步和差兩階時跨2步
#所以等同f(n) = f(n-1)+f(n-2)
#假設n = 5, 答案等同到3階的方法數+到4階的方法數
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

