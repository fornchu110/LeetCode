#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
# ��ù���Ʀr��, �ഫ���̶i��Ʀr

# By hash table ,time: O(n), space: O(k), k = 7, �N�Où���Ʀr�򥻤����ƶq
# �إߥXhash��ӵ۳W�h�����Y�i
# �o�D���q�k�쥪���X��n, �o�ˤ��Ψ��X�ĤG��
class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        # �����X�@�����[�`
        for i in s:
            res += hash[i]
        # ��[�L�Y�����^�h
        for i in range(1, len(s)):
            # I�O1���᭱�p�G��V��X, �h�N��NV��X-1, Ex: I = 1, V = 5, IV = 4
            if (s[i]=="V" or s[i]=="X") and s[i-1]=="I":
                res -= 2*hash["I"]
            # �P�W���P�z
            elif(s[i]=="L" or s[i]== "C") and s[i-1]=="X":
                res -= 2*hash["X"]
            elif(s[i]=="D" or s[i]== "M") and s[i-1]=="C":
                res -= 2*hash["C"]
        return res

# @lc code=end

