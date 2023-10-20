#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
# ����r��s�Mt, �p�Gs�Mt���r���@�Ҥ@�˥u�O���ܶ���return True, ���Mreturn False
# s�Mt���e���O�p�g�^��r��

# By hash, time: O(n), space: O(26), �]�r���̦h�N26��
# �N�Ĥ@�Ӧr��s�����e�ئ�hash, ���Xt�T�{�O�_�@�Ҥ@��
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # �`�N�u�n���פ��P���wFalse, �]�קKt��s���y��True�����p
        if len(s)!=len(t):
            return False
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in t:
            if i not in hash or hash[i]==0:
                return False
            else:
                hash[i] -= 1
        return True

# By sort, time: O(nlogn), space: O(logn)
# space = O(logn)��]�O�ƧǩҪ�O���Ŷ� 
# �o�D�]�i�H�N�r��sort��T�{�O�_�ۦP
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         # �`�Nstr�S��str.sort(), ��sorted()�i�H��str�Φ��|�^��list, �B�Ϊk�Osorted(str)�Ӥ�.sorted()
#         # �ܦ�list�����"".join(list)��^str
#         # split()�O�H���w�Ÿ������j, �q�{�O�ť�, ����Φb�o�سs��r���W
#         # �s��r��������list(str)�ഫ�Y�i
#         s = "".join(sorted(s))
#         t = "".join(sorted(t))
#         idx = len(s)-1
#         while idx>=0:
#             if s[idx]!=t[idx]:
#                 return False
#             idx -= 1
#         return True
    
# @lc code=end

