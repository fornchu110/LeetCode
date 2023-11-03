#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
# 給一字串s, return字串s中長度最長的子字串(不是子序列, 所以字元必須連續)

# By simulation, time: O(n^2), space: O(1)
# 想法是DP變形
# DP先初始化了長度最短的, 而回文有分從長度1擴展和從長度2擴展(奇數與偶數字元數量的回文串)
# 所以只有走訪s以每個index作為起點從長度1和長度2看是否回文至擴展到最大即可
class Solution:
    def expandAroundCenter(self, s, left, right):
        # s[left]==s[right]是重點, 當長度1時left本來就==right, 目的在於檢測長度2時是否回文
        while left >= 0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return left+1, right-1
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        n = len(s)
        for i in range(n):
            l1, r1 = self.expandAroundCenter(s, i, i)
            l2, r2 = self.expandAroundCenter(s, i, i+1)
            if r1-l1>end-start:
                start = l1
                end = r1
            if r2-l2>end-start:
                start = l2
                end = r2
        return s[start: end + 1]

# By DP, time: O(n^2), space:O(n^2)
# 長度為1必定為回文, 再一一增加長度看是否仍回文

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n<2:
#             return s
#         max_len = 1
#         # 初始的res, 也就是當最佳長度只有1時會return這個
#         res = s[0]
#         # dp[i][j] 表示 s[i..j] 是否是回文串
#         dp = [[False for j in range(n)] for i in range(n)]
#         for i in range(n):
#             dp[i][i] = True
        
#         # 回文要從長度最短的開始做才能DP, 後面更長的看更短的結果
#         for L in range(2, n + 1):
#             # 枚?左?界，左?界的上限?置可以?松一些
#             for i in range(n):
#                 # 由 L 和 i 可以确定右?界，即 j - i + 1 = L 得
#                 j = i+L-1
#                 # 如果右?界越界，就可以退出?前循?
#                 if j>=n:
#                     break
#                 # 最左的元素不等同最右的元素那必定不是回文
#                 if s[i]!=s[j]:
#                     dp[i][j] = False 
#                 else:
#                     # 當左右相同, 字串又只有1、2、3個元素那必定回文
#                     if L<4:
#                         dp[i][j] = True
#                     # 左右相同在字串長度>3時, 就看子字串相同與否才知道是否回文
#                     # 沒回文的字串左右加兩相同不會回文, 有回文的字串加上去才會繼續回文
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
                
#                 # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此???回文?度和起始位置           
#                 # 是回文且長度更長, 這段就是新答案
#                 if dp[i][j] and L>max_len:
#                     res = s[i:i+L]
#         return res

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         maxlen = 1
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 now = s[i:j+1]
#                 par = now[::-1]
#                 # print(now)
#                 if len(now)>maxlen and now==par:
#                     maxlen = len(now)
#                     res = now
#         if maxlen==1:
#             return s[0]
#         else:
#             return res

# @lc code=end

