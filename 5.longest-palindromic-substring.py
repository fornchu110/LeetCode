#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
# 倒﹃s, return﹃sい程﹃(ぃ琌, ┮じゲ斗硈尿)

# By simulation, time: O(n^2), space: O(1)
# 稱猭琌DP跑
# DP﹍て程祏, τゅΤだ眖1耎甶㎝眖2耎甶(计籔案计じ计秖ゅ﹃)
# ┮Τǐ砐s–index癬翴眖1㎝2琌ゅ耎甶程
class Solution:
    def expandAroundCenter(self, s, left, right):
        # s[left]==s[right]琌翴, 讽1leftセㄓ碞==right, ヘ浪代2琌ゅ
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
# 1ゲ﹚ゅ, 糤琌ごゅ

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n<2:
#             return s
#         max_len = 1
#         # ﹍res, 碞琌讽程ㄎΤ1穦return硂
#         res = s[0]
#         # dp[i][j] ボ s[i..j] 琌琌ゅ﹃
#         dp = [[False for j in range(n)] for i in range(n)]
#         for i in range(n):
#             dp[i][i] = True
        
#         # ゅ璶眖程祏秨﹍暗DP, 祏挡狦
#         for L in range(2, n + 1):
#             # 猅?オ?オ??竚?猀ㄇ
#             for i in range(n):
#                 # パ L ㎝ i 谔﹚? j - i + 1 = L 眔
#                 j = i+L-1
#                 # 狦?禫碞癶?玡碻?
#                 if j>=n:
#                     break
#                 # 程オじぃ单程じêゲ﹚ぃ琌ゅ
#                 if s[i]!=s[j]:
#                     dp[i][j] = False 
#                 else:
#                     # 讽オ, ﹃Τ123じêゲ﹚ゅ
#                     if L<4:
#                         dp[i][j] = True
#                     # オ﹃>3, 碞﹃籔笵琌ゅ
#                     # ⊿ゅ﹃オㄢぃ穦ゅ, Τゅ﹃穦膥尿ゅ
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
                
#                 # 璶 dp[i][L] == true Θミ碞ボ﹃ s[i..L] 琌ゅ???ゅ?㎝癬﹍竚           
#                 # 琌ゅ, 硂琿碞琌穝氮
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

