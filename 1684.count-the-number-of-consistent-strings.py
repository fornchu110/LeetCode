#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
# By hash: time: O(n), space: O(k), n = len(words), space k�̦h�u�|��26�ӭ^�� 
# �P�_���w�r�ꤤ���X�ӥu��allowed���e���r�źc��
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hash = dict()
        res = 0
        for i in allowed:
            if i not in hash:
                hash[i] = 1
        for i in words:
            # ��flag�P�_�O�_����allowed���r�Ųզ�
            flag = 1
            for j in i:
                if j not in hash:
                    flag = 0
                    break
            # flag = 1�N�����allowed�զ�, �_�hflag�|�O0
            if flag:
                res += 1
        return res
        
# @lc code=end

