#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
# ���@��r��, a1���ܦ^��ab, �]�N�Oa�Ma�᭱�@�Ӧr��b, x0�^��xx, �H������
# Ex: "a1b2c3d4e"�ഫ��"abbdcfdhe"

# By string proccessing, time: O(n), space: O(n)
# space: O(n)�O�]python���ઽ���̧ǭק�r��, ���n�B�z�ҥH�Τ@��arr list�A���ഫ�h��Ŷ�
# �Y��c��c++�����B�z�N�OO(1)
class Solution:
    def replaceDigits(self, s: str) -> str:
        n = len(s)
        arr = list(s)
        # ���Ʀ�m���r�����w�O���ƪ�, �ݩ_�Ʀ�m���r�����D�M���Ʀ�m�r�����۹��m�Y�i
        for i in range(1, n, 2):
            arr[i] = chr(ord(arr[i-1])+int(arr[i]))
        return "".join(arr)

# @lc code=end

