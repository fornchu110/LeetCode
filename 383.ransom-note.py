#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start

# By hash, time: O(max(m, n)), space: O(k), k = 26�]�N�O�p�g�^��r���ƶq, m = len(ransomNote), n = len(magazine)
# ��hash�����Xmagazine�N�֦����r���ƶq�x�s�_��, �A���XransomNote�ݯ�_��magazine�����r�����X��
# �`�N�^��r����hash�i�H��bitwise��, ���W�L32
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ��ransomNote��magazine�����w���i���magazine�զX�X��
        if len(ransomNote)>len(magazine):
            return False
        hash = {}
        for i in magazine:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in ransomNote:
            if i in hash:
                hash[i] -= 1
                if hash[i]<0:
                    return False
            else:
                return False
        return True
        # hash�}�l�o��q�i�H����collections.Counter()����
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)

        
# @lc code=end

