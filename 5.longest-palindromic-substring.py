#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
# ���@�r��s, return�r��s�����׳̪����l�r��(���O�l�ǦC, �ҥH�r�������s��)

# By simulation, time: O(n^2), space: O(1)
# �Q�k�ODP�ܧ�
# DP����l�ƤF���׳̵u��, �Ӧ^�妳���q����1�X�i�M�q����2�X�i(�_�ƻP���Ʀr���ƶq���^���)
# �ҥH�u�����Xs�H�C��index�@���_�I�q����1�M����2�ݬO�_�^����X�i��̤j�Y�i
class Solution:
    def expandAroundCenter(self, s, left, right):
        # s[left]==s[right]�O���I, �����1��left���ӴN==right, �ت��b���˴�����2�ɬO�_�^��
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
# ���׬�1���w���^��, �A�@�@�W�[���׬ݬO�_���^��

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n<2:
#             return s
#         max_len = 1
#         # ��l��res, �]�N�O��̨Ϊ��ץu��1�ɷ|return�o��
#         res = s[0]
#         # dp[i][j] ��� s[i..j] �O�_�O�^���
#         dp = [[False for j in range(n)] for i in range(n)]
#         for i in range(n):
#             dp[i][i] = True
        
#         # �^��n�q���׳̵u���}�l���~��DP, �᭱������ݧ�u�����G
#         for L in range(2, n + 1):
#             # �T?��?�ɡA��?�ɪ��W��?�m�i�H?�Q�@��
#             for i in range(n):
#                 # �� L �M i �i�H�̩w�k?�ɡA�Y j - i + 1 = L �o
#                 j = i+L-1
#                 # �p�G�k?�ɶV�ɡA�N�i�H�h�X?�e�`?
#                 if j>=n:
#                     break
#                 # �̥������������P�̥k�����������w���O�^��
#                 if s[i]!=s[j]:
#                     dp[i][j] = False 
#                 else:
#                     # ���k�ۦP, �r��S�u��1�B2�B3�Ӥ��������w�^��
#                     if L<4:
#                         dp[i][j] = True
#                     # ���k�ۦP�b�r�����>3��, �N�ݤl�r��ۦP�P�_�~���D�O�_�^��
#                     # �S�^�媺�r�ꥪ�k�[��ۦP���|�^��, ���^�媺�r��[�W�h�~�|�~��^��
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
                
#                 # �u�n dp[i][L] == true ���ߡA�N��ܤl�� s[i..L] �O�^��A��???�^��?�שM�_�l��m           
#                 # �O�^��B���ק��, �o�q�N�O�s����
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

