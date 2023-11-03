#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
# By hash and ord() and chr(), time: O(m+n), space: O(26), m��key����, n��message����
# space: O(26)�O�]��hash�Ψ��x�s26�ӭ^��r��
# ��key�q�Y������O����a~z, �Nmessage�ھڳo��key�ܴ��X��
# �зǫ�hash��, �o�D�]�i�H��index array����
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = list()
        # ��ord()�ӱo��ascii code, ��l�Ƭ�a
        ascii = ord('a')
        # �ع�����hash
        hash = dict()
        for i in key:
            # key���e���i�H����, �ҥH�n�P�_���bhash
            # ���F�p�g�^��u�|��' '(�Ů�)
            if i!=' ' and i not in hash:
                hash[i] = ascii
                # ���ӲĤ@���X�{���ǹ���ascii
                # python�S��k������r�Ű��B��
                ascii += 1
        # �B�zmessage
        for i in message:
            if i in hash:
                res.append(chr(hash[i]))
            else:
                res.append(' ')
        # ��''.join()�Nlist�ഫ���r��
        return ''.join(res)

# @lc code=end

