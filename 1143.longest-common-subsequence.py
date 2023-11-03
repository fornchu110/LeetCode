#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
# 一兩個字串text1和text2, 求兩者的最長公共子字串
# 注意子字串是連續的, 但可以不連續的存在text1或text2中
# Ex: ace和abcde的最長公共子字串是ace

# By DP, time: O(mn), space: O(mn), m = len(text1), n = len(text2)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp[i][j]代表text1前i個元素這一字串和text2前j個元素這一字串的最長公共子字串長度
        # 所以dp[i][j]實際上看到第i-1個text1字元和第j-1個text2,字元
        # 需要(n+1)*(m+1)是為了方便初始化dp[0][0], 也就是考慮前0個字元的邊界條件
        # 生成一個(m+1)*(n+1)大小初始化為0的二維陣列
        # 注意不能用dp = [[0]*(n+1)]*(m+1)來生成二維陣列, 否則會有m+1個連結在一起的[0]*(n+1)
        dp = [[0]*(n+1) for i in range(m+1)]
        # 因此這題狀態轉移式有兩種, 也就是說dp[i][j]有兩種可能的狀態轉移式

    
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 當text1[i-1]==text2[j-1]時, dp[i][j]等同於dp[i-1][j-1]+1
                # Ex: ac和bc的最長公共就是a和b的最長+1, 也就是1+1 = 2
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                # 當text1[i-1]!= text2[j-1]時, dp[i][j]等同於dp[i-1][j]或dp[i][j-1]
                # 此時dp[i][j]最少也會等同dp[i-1][j-1], 再分別考慮包含text[i-1]還是text[j-1]
                # 為什麼要考慮包含i-1或j-1?因為現在是求dp[i][j]!!!
                # Ex: ace和bc的最長公共字串是ac和bc的最長或ace和b的最長, 選大者
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # dp[m][n]就代表結果
        return dp[m][n]
        
# @lc code=end

