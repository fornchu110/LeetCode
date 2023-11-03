#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
# By string processing, time: O(n), space: O(1), n = len(s)
# return�p�g�r��, ��lower()�N��N�r��j�g�ഫ���p�g
# ���`�����ӬO���Xs��ord()�Mchr()��ascii�X���ഫ
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

# By bitwise, time: O(n), space: O(1)
# |32�O�ޥ�, �j��p��n�Oascii+32, ��32�O2^5�i�H��|�ӹF���j�g��p�g
# class Solution:
#     def toLowerCase(self, s: str) -> str:
#         return "".join(chr(asc | 32) if 65 <= (asc := ord(ch)) <= 90 else ch for ch in s)

# @lc code=end

