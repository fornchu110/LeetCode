#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#

# @lc code=start
# ���@�r���1~9, 10#~26#�Ҳզ�, �ä��O����a~i, j~z, �N�r���ഫ�������r��
# Ex: "10#11#12"�ഫ��"jkab"

# By string proccessing, time: O(n), space: O(1)
class Solution:
    def freqAlphabets(self, s: str) -> str:
        def get(st):
            # 1������p�ga, ���P��N"1"�ഫ��ascii 97��"a", �ҥH�O+96
            return chr(int(st)+96)
        # idx�ΨӪ��D�ثe�B�z�쪺�r���}, ��l�Ʀr��res
        idx, res = 0, ""
        while idx<len(s):
            # �C���n���ݫ��Ӧr���O�_��#, �ӧP�_�Oj~z�٬Oa~i
            # Ex: 12�M12#���������P, ���O�Oab�Ml
            # �`�Nc�y���]�O��s[i+2], �����O�����m
            if idx+2<len(s) and s[idx+2]=='#':
                res += get(s[idx:idx+2])
                idx += 2
            else:
                # ��+��r���s�_��, c�y����strcat
                res += get(s[idx])
            idx += 1
        return res

# @lc code=end

