#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
# 給一字串s, return s內的數字可以組合成多少種字母排列, 1~26分別代表a~z, 注意01並不等於1


# By DP, time: O(n), space: O(n)
# 因dp[n]只會用到dp[n-1]和dp[n-2], 可以優化為三變數空間, 也就是space = O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1]+[0]*n
        for i in range(1, n+1):
            if s[i-1]!='0':
                dp[i] += dp[i-1]
            if i>1 and s[i-2]!='0' and int(s[i-2:i])<=26:
                dp[i] += dp[i-2]
        return dp[n]

# 三變數作法, space: O(1)
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         # a = f[i-2], b = f[i-1], c = f[i]
#         a, b, c = 0, 1, 0
#         for i in range(1, n + 1):
#             c = 0
#             if s[i - 1] != '0':
#                 c += b
#             if i>1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
#                 c += a
#             a, b = b, c
#         return c
        
# @lc code=end

