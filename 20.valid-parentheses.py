#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
# �P�_s�����A���O�_valid

# By stack, time: O(n), space: O(n+6), n = len(s), 6 = pairs�Ұ�hash�᪺�Ŷ�
# ��list��@stack, append��push, pop�N���ݨ��X
class Solution:
    def isValid(self, s: str) -> bool:
        # ���׫D���Ƥ@�w�|�D�k
        if len(s)&1:
            return False    
        # ��ڤW�O�@��hash, {}�ҥH�Odict��Ƶ��c
        # ��hash���@�k�קK�F�@��if else
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for ch in s:
            # �J��)�B]�B}�ɱN���e���X, �˴��줣�X�k�t�諾��return False
            # �u�b�J��o�W���T�خɷ|�P�_False, �ҥH��invalid�P�_������, �L�k���X������return True
            if ch in pairs:
                #�O�ostack[-1]�O�˴�list���̫�@�Ӥ���
                if not stack or stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
            # �J��(�B[�B{�ɰ�push
            else:
                stack.append(ch)
        # ���X����stack���ťN���T, �����ťN����~, �ҥH��not
        # �W�����X�ɪ��˴��L�k�˴��X�I�쭫��(�B[�B{�����p, �ҥH�~�n�o��
        return not stack
     
# @lc code=end

