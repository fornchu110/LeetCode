#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
# ���@�r��s, return s�����Ʀr�i�H�զX���h�ֺئr���ƦC, 1~26���O�N��a~z, �`�N01�ä�����1


# By DP, time: O(n), space: O(n)
# �]dp[n]�u�|�Ψ�dp[n-1]�Mdp[n-2], �i�H�u�Ƭ��T�ܼƪŶ�, �]�N�Ospace = O(1)
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

# �T�ܼƧ@�k, space: O(1)
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

