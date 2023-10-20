#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
# ����r��word1�Mword2, �Hword1�}�lreturn�N��r��r���@�@����᪺�r��

# By double pointer and string processing, time: O(m+n), space: O(1), m = len(word1), n = len(word2)
# time = O(m+n)�O�]���O���X��Ӥ��P�r��
# ��while�j��qindex 0�}�l���[�Jword1[idx]�A�[�Jword2[idx]
# �b�r���٦����e�ɤ~�[�J, ���׬�2���r��idx�u���1, �קKindex out of range
# python�Τ����]�వ��, ���ݭnlist
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        # while�|���������r����׬ۦP������
        n = max(len(word1), len(word2))
        res = []
        while(n>0):
            if idx<len(word1):
                res.append(word1[idx])
            if idx<len(word2):
                res.append(word2[idx])
            idx += 1
            n -= 1
        # list��r��
        return "".join(res)
# @lc code=end

