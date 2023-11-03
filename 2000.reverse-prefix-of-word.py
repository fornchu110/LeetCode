<<<<<<< HEAD
#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
# ���r��word�M�ؼ�ch, �Nword���Ĥ@���X�{ch�H�e����������
# Ex: word: abcdefd, ch: d, return: dcbaefd

# By string processing, time: O(n), space: O(1) 
# �Q��python�������覡�B�z
# �Y�Oc�y���ϥ�double pointer, ��strchr()���ch��, �ϥΤ@��pointer���V�}�Y�@�ӫ��Vch�Ҧb��m
# �b�}�Y<ch��m������, ���O�洫��m�Ҧs�񪺦r���ñN�}�Y++, ch--, ��}�Y>=ch��m�K�N��洫����
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # ������Xch�Ĥ@���X�{����m, find���ch��index
        # �Ӧ]����[a:b]�u�|�B�z��b�e�@��, �ҥH�n+1, ����[a:b+1]�~�|a~b+1�Ҧ��r��
        # Ex: word: abcdefd, ch: d, ch�bindex3, i = 4
        i = word.find(ch)+1
        # ���ch�Ҧb��, return������ӳ���, ���઺�M�����઺
        # word[:i]�N���word�}�Y��ch, �᭱�A��o�Ӧr�갵[::-1]�]�N�O����
        # ����B�z����, +word[i]�]�N�Och�H�᪺�����Y�i
        # �ҥH�`�N�����������O((word[:i])[::-1])
        # �����word[:i:-1], �o���ܦ��˵ۨ��X��i���U�@�Ӧr������
        # Ex: word: abcdefd, ch: d, word[:i:-1] = df
        return word[:i][::-1]+word[i:]
        
# @lc code=end

=======
#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
# ���r��word�M�ؼ�ch, �Nword���Ĥ@���X�{ch�H�e����������
# Ex: word: abcdefd, ch: d, return: dcbaefd

# By string processing, time: O(n), space: O(1) 
# �Q��python�������覡�B�z
# �Y�Oc�y���ϥ�double pointer, ��strchr()���ch��, �ϥΤ@��pointer���V�}�Y�@�ӫ��Vch�Ҧb��m
# �b�}�Y<ch��m������, ���O�洫��m�Ҧs�񪺦r���ñN�}�Y++, ch--, ��}�Y>=ch��m�K�N��洫����
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # ������Xch�Ĥ@���X�{����m, find���ch��index
        # �Ӧ]����[a:b]�u�|�B�z��b�e�@��, �ҥH�n+1, ����[a:b+1]�~�|a~b+1�Ҧ��r��
        # Ex: word: abcdefd, ch: d, ch�bindex3, i = 4
        i = word.find(ch)+1
        # ���ch�Ҧb��, return������ӳ���, ���઺�M�����઺
        # word[:i]�N���word�}�Y��ch, �᭱�A��o�Ӧr�갵[::-1]�]�N�O����
        # ����B�z����, +word[i]�]�N�Och�H�᪺�����Y�i
        # �ҥH�`�N�����������O((word[:i])[::-1])
        # �����word[:i:-1], �o���ܦ��˵ۨ��X��i���U�@�Ӧr������
        # Ex: word: abcdefd, ch: d, word[:i:-1] = df
        return word[:i][::-1]+word[i:]
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
