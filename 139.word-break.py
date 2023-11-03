#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
# 給字串s和一堆字串wordDict, return字串s能否分割成wordDict內字串
# 不要求wordDict內所有字串都要使用到, 只要能剛好分割即可, 且wordDict內的字串可以重複使用
# Ex: s = "leetcode", wordDict = ["leet", "code", "abc"], return True
# Ex: s = "penapple", wordDict = ["pen", pple], return False
# Ex: s = "leetleet", wordDict = ["leet"], return True

# By DP, time: O(n^2), space: O(n), 其中n = len(s)
# 重點在於wordDict內的字串可以重複使用, 所以想成將s分割成兩段
# 最後一段是wordDict子字串, 前面那段又可以被分割, 那整段就可被分割
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[i]代表前i個字元組成的字串能否被分割成wordDict內所有字串
        dp = [False]*(n+1)
        dp[0] = True
        # 以i為中介點分割, 
        for i in range(n):
            for j in range(i+1,n+1):
                # j必定比i大, 若dp[i]可以被分割成wordDict, 且i開始到j也在wordDict內, 那就代表dp[j]也是True
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[n]
    
# @lc code=end

