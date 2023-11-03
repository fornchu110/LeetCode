#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start

# By double pointer, time: O(n+m), space: O(1) 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        # python可以這樣判斷, ==就代表True, !=就代表False
        return i == n

# # By DP
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         n, m = len(s), len(t)
#         f = [[0] * 26 for _ in range(m)]
#         f.append([m] * 26)

#         for i in range(m - 1, -1, -1):
#             for j in range(26):
#                 f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
        
#         add = 0
#         for i in range(n):
#             if f[add][ord(s[i]) - ord('a')] == m:
#                 return False
#             add = f[add][ord(s[i]) - ord('a')] + 1
        
#         return True

# @lc code=end

