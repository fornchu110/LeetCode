<<<<<<< HEAD
#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
# By hash, time: O(n), space: O(1), n�Olen(sentence)
# �P�_sentence�����S�X�{�L�Ҧ��^��p�g�r��
# �o�D�]���T�wkey���ƶq, �]�i�H��ascii�X�ϥ�ord()�t�Xindex array��
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # ��hash
        hash = dict()
        cnt = 0
        # ��r�Ŭ��S�X�{�L���r��, ��Jhash�é�cnt+1
        # ���X�{�L�N����
        for i in sentence:
            if i not in hash:
                hash[i] = 1
                cnt += 1
        # �̫�ݬO�_��J�F����26�Ӧr��
        return cnt==26
        
# @lc code=end

=======
#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
# By hash, time: O(n), space: O(1), n�Olen(sentence)
# �P�_sentence�����S�X�{�L�Ҧ��^��p�g�r��
# �o�D�]���T�wkey���ƶq, �]�i�H��ascii�X�ϥ�ord()�t�Xindex array��
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # ��hash
        hash = dict()
        cnt = 0
        # ��r�Ŭ��S�X�{�L���r��, ��Jhash�é�cnt+1
        # ���X�{�L�N����
        for i in sentence:
            if i not in hash:
                hash[i] = 1
                cnt += 1
        # �̫�ݬO�_��J�F����26�Ӧr��
        return cnt==26
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
