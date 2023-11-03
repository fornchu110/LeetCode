<<<<<<< HEAD
#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
# ��X���wwords�Ĥ@�Ӱj�媺�r��

# By string proccessing, time: O(n), space: O(1), n = words�����r����
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            # �`�Nreversed()��^���O���N��, �n��list()������list�Υ�"".join()�������r��
            tmp = "".join(reversed(i))
            if tmp==i:
                return i
        return ""

# By double pointerm time: O(n), space: O(1)
# ���ϥ�reversed()���@�k, c�y���]�O�o�˼g
# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         # �Τ@�Ө禡�P�_��U�r��O�_�j��
#         def isPalindrome(word: str) -> bool:
#             n = len(word)
#             # �q�r���Y����m�@��pointer, �T�{�Y���O�_�ۦP
#             l, r = 0, n - 1
#             while l < r:
#                 # ���~�r�����ۦP�N��S�j��
#                 if word[l]!=word[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             # �]���r�ꤴ�Sreturn false�N��j��
#             return True
        
#         # ?�ǹM?�r�Ŧ�??�A�p�G�J��^��r�Ŧ�?��^�A���J��?��^�Ŧr�Ŧ�
#         for i in words:
#             if isPalindrome(i):
#                 return i
#         # ���X���N��S���j��r��
#         return ""
        
# @lc code=end

=======
#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
# ��X���wwords�Ĥ@�Ӱj�媺�r��

# By string proccessing, time: O(n), space: O(1), n = words�����r����
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            # �`�Nreversed()��^���O���N��, �n��list()������list�Υ�"".join()�������r��
            tmp = "".join(reversed(i))
            if tmp==i:
                return i
        return ""

# By double pointerm time: O(n), space: O(1)
# ���ϥ�reversed()���@�k, c�y���]�O�o�˼g
# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         # �Τ@�Ө禡�P�_��U�r��O�_�j��
#         def isPalindrome(word: str) -> bool:
#             n = len(word)
#             # �q�r���Y����m�@��pointer, �T�{�Y���O�_�ۦP
#             l, r = 0, n - 1
#             while l < r:
#                 # ���~�r�����ۦP�N��S�j��
#                 if word[l]!=word[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             # �]���r�ꤴ�Sreturn false�N��j��
#             return True
        
#         # ?�ǹM?�r�Ŧ�??�A�p�G�J��^��r�Ŧ�?��^�A���J��?��^�Ŧr�Ŧ�
#         for i in words:
#             if isPalindrome(i):
#                 return i
#         # ���X���N��S���j��r��
#         return ""
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
