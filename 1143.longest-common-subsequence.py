<<<<<<< HEAD
#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
# �@��Ӧr��text1�Mtext2, �D��̪��̪����@�l�r��
# �`�N�l�r��O�s��, ���i�H���s�򪺦s�btext1��text2��
# Ex: ace�Mabcde���̪����@�l�r��Oace

# By DP, time: O(mn), space: O(mn), m = len(text1), n = len(text2)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp[i][j]�N��text1�ei�Ӥ����o�@�r��Mtext2�ej�Ӥ����o�@�r�ꪺ�̪����@�l�r�����
        # �ҥHdp[i][j]��ڤW�ݨ��i-1��text1�r���M��j-1��text2,�r��
        # �ݭn(n+1)*(m+1)�O���F��K��l��dp[0][0], �]�N�O�Ҽ{�e0�Ӧr������ɱ���
        # �ͦ��@��(m+1)*(n+1)�j�p��l�Ƭ�0���G���}�C
        # �`�N�����dp = [[0]*(n+1)]*(m+1)�ӥͦ��G���}�C, �_�h�|��m+1�ӳs���b�@�_��[0]*(n+1)
        dp = [[0]*(n+1) for i in range(m+1)]
        # �]���o�D���A�ಾ�������, �]�N�O��dp[i][j]����إi�઺���A�ಾ��

    
        for i in range(1, m+1):
            for j in range(1, n+1):
                # ��text1[i-1]==text2[j-1]��, dp[i][j]���P��dp[i-1][j-1]+1
                # Ex: ac�Mbc���̪����@�N�Oa�Mb���̪�+1, �]�N�O1+1 = 2
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                # ��text1[i-1]!= text2[j-1]��, dp[i][j]���P��dp[i-1][j]��dp[i][j-1]
                # ����dp[i][j]�̤֤]�|���Pdp[i-1][j-1], �A���O�Ҽ{�]�ttext[i-1]�٬Otext[j-1]
                # ������n�Ҽ{�]�ti-1��j-1?�]���{�b�O�Ddp[i][j]!!!
                # Ex: ace�Mbc���̪����@�r��Oac�Mbc���̪���ace�Mb���̪�, ��j��
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # dp[m][n]�N�N���G
        return dp[m][n]
        
# @lc code=end

=======
#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
# �@��Ӧr��text1�Mtext2, �D��̪��̪����@�l�r��
# �`�N�l�r��O�s��, ���i�H���s�򪺦s�btext1��text2��
# Ex: ace�Mabcde���̪����@�l�r��Oace

# By DP, time: O(mn), space: O(mn), m = len(text1), n = len(text2)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp[i][j]�N��text1�ei�Ӥ����o�@�r��Mtext2�ej�Ӥ����o�@�r�ꪺ�̪����@�l�r�����
        # �ҥHdp[i][j]��ڤW�ݨ��i-1��text1�r���M��j-1��text2,�r��
        # �ݭn(n+1)*(m+1)�O���F��K��l��dp[0][0], �]�N�O�Ҽ{�e0�Ӧr������ɱ���
        # �ͦ��@��(m+1)*(n+1)�j�p��l�Ƭ�0���G���}�C
        # �`�N�����dp = [[0]*(n+1)]*(m+1)�ӥͦ��G���}�C, �_�h�|��m+1�ӳs���b�@�_��[0]*(n+1)
        dp = [[0]*(n+1) for i in range(m+1)]
        # �]���o�D���A�ಾ�������, �]�N�O��dp[i][j]����إi�઺���A�ಾ��

    
        for i in range(1, m+1):
            for j in range(1, n+1):
                # ��text1[i-1]==text2[j-1]��, dp[i][j]���P��dp[i-1][j-1]+1
                # Ex: ac�Mbc���̪����@�N�Oa�Mb���̪�+1, �]�N�O1+1 = 2
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                # ��text1[i-1]!= text2[j-1]��, dp[i][j]���P��dp[i-1][j]��dp[i][j-1]
                # ����dp[i][j]�̤֤]�|���Pdp[i-1][j-1], �A���O�Ҽ{�]�ttext[i-1]�٬Otext[j-1]
                # ������n�Ҽ{�]�ti-1��j-1?�]���{�b�O�Ddp[i][j]!!!
                # Ex: ace�Mbc���̪����@�r��Oac�Mbc���̪���ace�Mb���̪�, ��j��
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # dp[m][n]�N�N���G
        return dp[m][n]
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
