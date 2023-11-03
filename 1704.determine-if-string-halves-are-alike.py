#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
# ���@�r��, �N�r��q�����@�b��ݨ��䪺aeiou, AEIOU�o�ǥ������ƶq�O�_�ۦP, �ۦPreturn true, �_�hfalse

# By string proccessing, time: O(n), space: O(n)), n�O���w�r�����
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # �����إߤ@�Ӭd������Ϊ��r��, �P�_���@�b���r�ꤧ�r���O�_�s�b���Y�i
        # ���ݭn�ϥ�hash, �����ӬO�P�z
        # c�y���i�H��strchr()�F�������ĪG, ���ؤ@��VOWELS�r�갵���d��Ϊ�hash
        # strchr(s, ch)�N��ch���s���Ĥ@���X�{����m, �Y�����|�^�Ǧ�}�S���^��NULL, �]���i�H�ΨӰ��P�_ch�O�_�s�bs��
        VOWELS = "aeiouAEIOU"
        # list����s[a:b], a�O�_�Ib�O���I, �S�ѼƴN�q�{index 0�}�l, ���ݵ���
        a, b = s[:len(s)//2], s[len(s)//2:]
        return sum(c in VOWELS for c in a) == sum(c in VOWELS for c in b)
        
# @lc code=end

