#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
# ���r��s�M�@��r��wordDict, return�r��s��_���Φ�wordDict���r��
# ���n�DwordDict���Ҧ��r�곣�n�ϥΨ�, �u�n���n���ΧY�i, �BwordDict�����r��i�H���ƨϥ�
# Ex: s = "leetcode", wordDict = ["leet", "code", "abc"], return True
# Ex: s = "penapple", wordDict = ["pen", pple], return False
# Ex: s = "leetleet", wordDict = ["leet"], return True

# By DP, time: O(n^2), space: O(n), �䤤n = len(s)
# ���I�b��wordDict�����r��i�H���ƨϥ�, �ҥH�Q���Ns���Φ���q
# �̫�@�q�OwordDict�l�r��, �e�����q�S�i�H�Q����, ����q�N�i�Q����
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[i]�N��ei�Ӧr���զ����r���_�Q���Φ�wordDict���Ҧ��r��
        dp = [False]*(n+1)
        dp[0] = True
        # �Hi�������I����, 
        for i in range(n):
            for j in range(i+1,n+1):
                # j���w��i�j, �Ydp[i]�i�H�Q���Φ�wordDict, �Bi�}�l��j�]�bwordDict��, ���N�N��dp[j]�]�OTrue
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[n]
    
# @lc code=end

