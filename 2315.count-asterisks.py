#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
# ���r��s, return�������'|'�H�~��'*'�ƶq

# By simulation, time: O(n), space: O(1)
# ��}��, �@�˱q�Y���X���u�n�ŦX����ɹJ��'*'�p�ƴN�n, �����B�~�N��L�r����Jtmp
class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        flag = 1
        for ch in s:
            # �b�J��"|"�ɰ��P�_, �]��flag�u��0��1�ҥH��not���ܭȴN�n
            if ch=='|':
                # ��not�N���ݭn��if flag�ӧP�_flag���A, �ϥ��J��'|'�N�n���flag
                flag = not flag
            # ��flag��1�B�O'*'�ɼW�[�p��
            elif flag and ch=='*':
                res += 1
        return res    

# # By simulation, time: O(n), space: O(n)
# # �q�Y���Xs, �N����"|"�����H�~���r����Jtmp, �A���Xtmp��"*"�ƶq
# class Solution:
#     def countAsterisks(self, s: str) -> int:
#         tmp = []
#         res = 0
#         # �Q��flag���D�ثe�O�_�b����"|"����, �]�N�O�b�J��Ĥ@��"|"�ɱNflag�]��0
#         flag = 1
#         for ch in s:
#             if flag:
#                 tmp.append(ch)
#                 if ch=="|":
#                     flag = 0
#             else:
#                 if ch=="|":
#                     flag = 1
#         for ch in tmp:
#             if ch=="*":
#                 res += 1
#         return res
        
# @lc code=end

