#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
# ���@�r��, �u���alphanumeric character�O�_�j��, �]�N�O�r���M�Ʀr
# �`�N�@�Ӧr�����j�p�g��P�@��

# By double pointer and isalnnum(), time: O(n), space: O(1)
# isalnum()�P�_�r���M�Ʀr, isalpha()�P�_�r��
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            # ���ϥ�if�Mcontinue�N�bnot�e���[��while l<r and 
            # �N�Dalphanumeric character
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            # ����o�N��Oalnum, �Y�g�Llower�o���۵�return False
            if s[l].lower()!=s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

# By isalnum() and lower and[::-1], time: O(n), space: O(n)
# �Q��isalnum()�P�_�r���O�_�Oalphanumeric character, �O���ܥ�lower()�ഫ���p�g�[�Jres��
# �̫�P�_res�O�_���P�qres[::-1]�Y�i
# �u�Ʀ�space = O(1)���ܴN�n�b��r��s���P�_, ���@�ˬO��isalnum()�Mlower, �u�O���w�n��double pointer
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         res = []
#         for i in s:
#             if i.isalnum():
#                 # �Ʀr�M�p�g���|�Q.lower()�ഫ, �u���j�g�~�Q�v�T
#                 # �o���.upper()�]�O�P�z
#                 res.append(i.lower())
#         res = "".join(res)
#         # �W�����@��g�k, �C��ͦ���
#         # res = "".join(ch.lower() for ch in s if ch.isalnum())
#         return res==res[::-1]

# By double pointer and ord(), time : O(n), space: O(1)
# �q�Y�ݩM���ݤ��O�P�_��U���V��alphanumeric characters�O�_�ŦX�j��n�D
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l = 0
#         r = len(s)-1
#         while l<r:
#             if not (ord('a')<=ord(s[l])<=ord('z') or ord('A')<=ord(s[l])<=ord('Z') or ord('0')<=ord(s[l])<=ord('9')):
#                 l += 1
#                 continue
#             elif not (ord('a')<=ord(s[r])<=ord('z') or ord('A')<=ord(s[r])<=ord('Z') or ord('0')<=ord(s[r])<=ord('9')):
#                 r -= 1
#                 continue
#             if ord('a')<=ord(s[l])<=ord('z'):
#                 print('1')
#                 if not (ord(s[l])==ord(s[r]) or ord(s[l])==ord(s[r])+32):
#                     print(s[l], s[r])
#                     return False
#                 else:
#                     l += 1
#                     r -= 1
#             elif ord('A')<=ord(s[l])<=ord('Z'):
#                 if not (ord(s[l])==ord(s[r]) or ord(s[l])==ord(s[r])-32):
#                     print(s[l], s[r])
#                     return False
#                 else:
#                     l += 1
#                     r -= 1
#             elif ord('0')<=ord(s[l])<=ord("9"):
#                 if ord(s[l])!=ord(s[r]):
#                     print(s[l], s[r])
#                     return False
#                 else:
#                     l += 1
#                     r -= 1
#         return True
        
# @lc code=end

